// Enter the existing durable inherited-owner protocol before evaluating the
// checkpoint CLI. Its nested declaration writer must reuse this same owner.
import {withDistArtifactOwnership} from "./lib/dist-artifact-ownership.mts";
import {runOwnedDistArtifactEntry} from "./lib/dist-artifact-lock.mts";
import {isDirectRunUrl} from "./lib/direct-run.mjs";
export async function runCheckpoint608(args=process.argv.slice(2)) {
 if(args.length!==1||!/^(runtime|unified-[0-5]|middle|sdk-[0-1]|tail|complete)$/.test(args[0]))throw new Error('Invalid fixed checkpoint stage');
 return withDistArtifactOwnership(process.cwd(),()=>runOwnedDistArtifactEntry(new URL("./build-checkpoint608.mts", import.meta.url).href,args));
}
if(isDirectRunUrl(process.argv[1],import.meta.url)) {
 void runCheckpoint608().catch(error=>{console.error(error);process.exitCode=1;});
}
