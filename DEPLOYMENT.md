# Deployment and verification

Target **stable Studionet**, not the Studio-dev release-candidate preview:

- Studio: https://studio.genlayer.com/contracts
- RPC: https://studio.genlayer.com/api
- Chain ID: 61999
- Explorer: https://explorer-studio.genlayer.com

The canonical source pins the runner used by stable Studio's v0.2.16 examples:
`py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`.
A newer runner being available does not imply that the stable deployed runner should be silently changed. GenVM lint must validate the exact pinned SDK. The SDK response field is `Response.status`; some narrative docs show `status_code`, so the actual pinned SDK is authoritative.

## Procedure

1. Install requirements, run tests and `genvm-lint check contracts/traceverdict.py`.
2. Commit and push source and small synthetic fixture files to main. Record that commit SHA and the source's raw-byte SHA-256/length. Pin fixture URLs to that commit.
3. Load the exact source in Studio. Use the Studio-provided account and **Normal / Full Consensus**, with no constructor arguments. Do not enable leader-only mode.
4. Deploy once, save the transaction ID immediately, and follow that same ID until finalization and successful GenVM execution. Read the deployed code back and compare its complete bytes against the repository.
5. Call `submit` with the committed claim, canonical manifest and empty previous ID. Wait for successful finalization. Obtain the resulting record ID from return/state.
6. Call `evaluate(record_id)` with Full Consensus. Wait for finalized SUCCESS and inspect leader plus validator votes, then read `get_record`, `get_counts` and `get_history` from finalized state.
7. Recompute the decision hash using the documented preimage. Preserve raw receipts, final record, source comparison and manifest. Push live-verification documentation. The documentation commit may be later than the deployed source commit, but must not change canonical source.

Use `python scripts/audit_record.py ADDRESS docs/final-record.json` to independently recompute a recorded verdict hash. This offline command proves encoding consistency, not that the JSON was retrieved from chain; the receipts and live reads establish that association.

The live deployment address, transaction links, actual results and limitations are recorded in [LIVE_VERIFICATION.md](docs/LIVE_VERIFICATION.md). No receipt is successful merely because a transaction was submitted or finalized; inspect execution success separately.
