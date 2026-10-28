// Diagnostic-only observation of the pinned native API. Never build authority.
const observed=new WeakSet();
const methods={API:['parseConfigFile','createSnapshot','close'],Program:[
 'getConfigFileParsingDiagnostics','getProgramDiagnostics','getGlobalDiagnostics',
 'getSyntacticDiagnostics','getBindDiagnostics','getSemanticDiagnostics','emitToString','getSourceFileNames']};
const monotonic=()=>Number(process.hrtime.bigint())/1e6;
const stderr=event=>process.stderr.write(JSON.stringify({kind:'NATIVE_API_PHASE608',pid:process.pid,...event})+'\n');
export function observeNativeApi608(api,emit=stderr,now=monotonic){
 const state={failed:false};
 const clock=()=>{try{const value=now();if(Number.isFinite(value))return value;}catch{}state.failed=true;return null;};
 const report=event=>{try{emit(event);}catch{state.failed=true;}};
 const patches=[];
 for(const [type,names] of Object.entries(methods)){
  const prototype=api[type]?.prototype;
  if(!prototype||observed.has(prototype))throw new Error('native API already observed or missing');
  for(const name of names){
   const descriptor=Object.getOwnPropertyDescriptor(prototype,name);
   if(typeof descriptor?.value!=='function'||!descriptor.writable)throw new Error('unsupported native API '+type+'.'+name);
   patches.push({prototype,name,descriptor,label:type+'.'+name});
  }
 }
 for(const {prototype,name,descriptor,label} of patches){
  const original=descriptor.value;
  Object.defineProperty(prototype,name,{...descriptor,value:async function(...args){
   const started=clock();report({method:label,phase:'start',monotonic_ms:started});
   let status='failed';
   try {const result=await Reflect.apply(original,this,args);status='returned';return result;}
   finally {const ended=clock();report({method:label,phase:'end',status,duration_ms:started===null||ended===null?null:Math.max(0,ended-started)});}
  }});
 }
 for(const type of Object.keys(methods))observed.add(api[type].prototype);
 return state;
}
function hasPreload(argv,observer){
 for(let i=0;i<argv.length;i++){
  const arg=argv[i];
  if(arg==='--'||!arg.startsWith('-'))return false;
  if(arg==='--import'){if(argv[++i]===observer)return true;}
  else if(arg==='--import='+observer)return true;
 }
 return false;
}
export function propagateNativeObserver608(childProcess,observer,nodeExecutable=process.execPath){
 const original=childProcess.spawn;
 childProcess.spawn=function(command,args,options){
  if(command!==nodeExecutable)return Reflect.apply(original,this,arguments);
  const argv=Array.isArray(args)?args:[];
  const settings=(Array.isArray(args)||args==null)?options:args;
  return original.call(this,command,hasPreload(argv,observer)?argv:['--import',observer,...argv],settings);
 };
}
