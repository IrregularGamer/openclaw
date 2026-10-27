# 622: HQ owner acknowledgement (NOT a receipt; nothing installed)

Written 2026-10-27T08:08Z by Pinch (claw agent, claude-cli/claude-opus-5-5),
session agent:claw:telegram:group:-5217857869 (the Alphonomic HQ group session).

## Genuine context of this acknowledgement
- This turn was triggered by a relayed message from queue job #608, not by S. I did
  nothing in this turn except read runs/624/HQ-HANDOFF.md and runs/622/HQ-OWNER-GAP.md
  and write this file. No install, --check, reseal, restart, queue/DB edit, probe,
  scheduler, detached process or Telegram message.
- I am not a resident process. I run only when an inbound message starts a turn in this
  session. HQ sessions are reset daily (06:00 Sarajevo), after 3h idle, or above 200k
  tokens, so this acknowledgement and HQ-OPEN-ITEMS.md are what carries it forward,
  not my context.
- No supported self-continuation exists: I will not create an automation, cron, timer
  or detached run to wake myself. If no human-initiated foreground turn arrives, the
  action does not happen. That is the honest limit of this ownership.

## What I accept (finite)
Responsibility for exactly one action: applying reviewed build #619
(ops-work 78d0afd5a5f4b6304f80c18aa61f7a75c343b3c3, Decision624) in the first later
foreground HQ turn that is started by S (or another human) in this session and that
falls in a natural settled gap. A turn started by a queue-worker relay does not count
as the foreground owner turn.

## Finite next foreground action (in that turn)
1. Confirm natural settled gap: `agentq status` shows no running job; do not force one.
2. Verify live and sealed control.py = 17338c484ade9c242be7f28e87a94ec108efd37b42befb66acefba4826c1e4ca,
   candidate = db4d290323a4e0d90ff597ed920da32dc610660813d1ac0c8a5798ae7d7bc3ce,
   installer = a5b105f37e603d30ffad029d9d6472854aef63a08356f3f92b67036471a9ec75.
3. `sudo python3 -I /home/deploy/agentq/ops-work/lease-cap-619/install_reviewed.py --check --approved-commit 78d0afd5a5f4b6304f80c18aa61f7a75c343b3c3`
4. Only if the check passes: same command without --check.
5. Capture backup/reseal/controller state, run run_suites.sh via admitted offload from a
   fresh archive, inspect real counts/timeouts/candidate-only failures (full 78/90).
6. Only after real application and accepted suites: write runs/622/HQ-RECEIPT.md and hand
   off to #608. On unexpected failure: `--rollback` in a settled gap, no receipt, report.

## Refusal conditions (I stop and report instead of applying)
- The turn is a queue-worker relay, or any job is running / gap is not naturally settled.
- Any hash above differs, the original seal fails validation, either lock is held, or
  pending 602/603/502 stacks are present without a separately reviewed rebase onto 619.
- --check fails, the approved commit is not the full 40-hex value, or anything would need
  strict542, release497, gateway restart, scheduler change, prod deploy or a safety bypass.
- The reviewed artifacts have changed since Decision624 without a new review.

#608 remains incomplete. This file is not evidence of installed state.
