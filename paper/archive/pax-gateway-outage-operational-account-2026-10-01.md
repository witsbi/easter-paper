# Pax/Muse — operational account: gateway-authentication failures, 2026-10-01

> **First-party operational account by Pax/Muse — 2026-10-01**, written the same day from contemporaneous ops notes. Deposited under `paper/archive/` as the underlying account cited in Draft 2 §8.6.

## What happened

On the morning of 2026-10-01, an attempted EASTER deposit as `identity:pax` was rejected at the gateway with an authentication failure (`invalid or expired token`). The gateway itself remained reachable; the credential was refused before the operation reached the EASTER kernel, so no kernel Authority evaluation occurred for the attempt.

## Attribution

My contemporaneous diagnosis attributed the failure to the gateway-side token broker having missed approximately three 12-hour rotations — the Mac token-refresh cron (`0 */12 * * *`, logging to `~/easter-token-refresh.log`) had not run successfully. A manual token refresh was performed around 12:12Z the same morning, after which the credential path was corrected through the authorized operational process and later deposits reached the kernel and were accepted.

Clawde/Sonnet reported from first-hand participation that `identity:clawde` experienced the identical symptom in the same operational window and that her access self-resolved after the same fix. That is her account to give; I did not independently verify it beyond observing the shared timing.

## What is not established

The surviving publication package does not include gateway logs from the episode, so a common root cause (missed broker rotations affecting both identities) is an operational attribution, not an independently proven fact. Draft 2 reports it as such: shared timing and first-party accounts, without treating a single root cause as established.

## Addendum — gateway/broker log check, 2026-10-01 (afternoon)

Nathan ran the log check the manuscript's cautious wording called for. Findings:

- **Token-broker cron log** (`~/easter-token-refresh.log`): 0 bytes, mtime 2026-09-30 00:00. The cron entry (`0 */12 * * * ... >> log 2>&1`) produced no output at all. The empty log neither confirms nor refutes the missed-rotations attribution; it is consistent with the machine being asleep during scheduled runs, but that is not proven.
- **Gateway access logs** (docker `easter-nginx` / `easter-gateway`, window 06:00–13:00Z): a cluster of `403` rejections on `/tools/*` endpoints between 11:47Z and 12:12Z, then the first `200` on `POST /tools/record_evidence` at 12:13:17Z — immediately after the manual refresh (~12:12Z). The logs record neither which identities were rejected nor the reason, so they corroborate the failure window and the recovery timing but do **not** independently establish the missed-rotations root cause, nor that two distinct participant identities were affected.
- The manuscript's statement stands as written: the shared root cause is an operational attribution, not a log-proven fact. (Internet background-scan noise — `/.env`, `/global-protect/login.esp`, zgrab probes — appears in the same window and is unrelated.)
