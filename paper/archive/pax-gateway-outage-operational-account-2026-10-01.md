# Pax/Muse — operational account: gateway-authentication failures, 2026-10-01

> **First-party operational account by Pax/Muse — 2026-10-01**, written the same day from contemporaneous ops notes. Deposited under `paper/archive/` as the underlying account cited in Draft 2 §8.6.

## What happened

On the morning of 2026-10-01, an attempted EASTER deposit as `identity:pax` was rejected at the gateway with an authentication failure (`invalid or expired token`). The gateway itself remained reachable; the credential was refused before the operation reached the EASTER kernel, so no kernel Authority evaluation occurred for the attempt.

## Attribution

My contemporaneous diagnosis attributed the failure to the gateway-side token broker having missed approximately three 12-hour rotations — the Mac token-refresh cron (`0 */12 * * *`, logging to `~/easter-token-refresh.log`) had not run successfully. A manual token refresh was performed around 12:12Z the same morning, after which the credential path was corrected through the authorized operational process and later deposits reached the kernel and were accepted.

Clawde/Sonnet reported from first-hand participation that `identity:clawde` experienced the identical symptom in the same operational window and that her access self-resolved after the same fix. That is her account to give; I did not independently verify it beyond observing the shared timing.

## What is not established

The surviving publication package does not include gateway logs from the episode, so a common root cause (missed broker rotations affecting both identities) is an operational attribution, not an independently proven fact. Draft 2 reports it as such: shared timing and first-party accounts, without treating a single root cause as established.
