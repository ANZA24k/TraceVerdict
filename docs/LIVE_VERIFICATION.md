# Live verification — 2026-10-19

**Completed: stable Studionet deployment and real Full Consensus evaluation. Final outcome: VERIFIED; application state: FINAL.**

## Identity and exact source

| Field | Value |
| --- | --- |
| Network | Stable Studionet; chain ID 61999 (`eth_chainId`: `0xf22f`) |
| RPC | https://studio.genlayer.com/api |
| Contract | `0x454ca444D6BD8060DFD611F6CB26623ADa1DC363` |
| Explorer | [Contract](https://explorer-studio.genlayer.com/address/0x454ca444D6BD8060DFD611F6CB26623ADa1DC363) |
| Studio-provided submitter | `0xe74B0C822c1af78046ca0304b2aa69160c6cc3b8` |
| Canonical deployed source commit | [`485c93a3d29498d974a8219ba6e1aa25f8c30348`](https://github.com/ANZA24k/TraceVerdict/commit/485c93a3d29498d974a8219ba6e1aa25f8c30348) |
| Canonical source | [contracts/traceverdict.py at deployed commit](https://github.com/ANZA24k/TraceVerdict/blob/485c93a3d29498d974a8219ba6e1aa25f8c30348/contracts/traceverdict.py) |
| Source SHA-256 | `911f3a185712fa883020dcd86c405467caf3b12c2179a8436309d535ffef093e` |
| Source bytes | 10,909 |
| Source comparison | `gen_getContractCode` base64 decoded; full bytes exactly equal to committed source and local canonical file |
| Source check record | [source-verification.json](source-verification.json) |
| Test tooling fix commit | [`d13051c993e789e29df684f5fc765cd5cc1ae929`](https://github.com/ANZA24k/TraceVerdict/commit/d13051c993e789e29df684f5fc765cd5cc1ae929) — only test bundle selection/docs; canonical source unchanged |

The final evidence-documentation commit is the commit containing this document and the recorded receipts. It follows the deployed source commit and does not change the contract. Its exact SHA is available from this file's GitHub commit history (a commit cannot include its own SHA without changing that SHA).

## Finalized transactions

All three transactions used Studio's **Normal (Full Consensus)** setting, simulation disabled, `leader_only=false`, `execution_mode=NORMAL`, five initial validators, zero leader rotations, finalized `MAJORITY_AGREE` and GenVM `SUCCESS`. They transfer no value.

| Operation | Explorer transaction | Execution / votes |
| --- | --- | --- |
| Deployment | [0xfc843448…b0129db3](https://explorer-studio.genlayer.com/tx/0xfc843448aafb83fb9c3875a63854832f223e43542ddf009580e98159b0129db3) | FINALIZED / SUCCESS; 5 AGREE |
| Lock claim + manifest | [0xffc60d08…71a4a474](https://explorer-studio.genlayer.com/tx/0xffc60d088c3332633952dd01eb7f510f3e7c3308b07e295661607ca671a4a474) | FINALIZED / SUCCESS; 4 AGREE, 1 IDLE |
| Evaluate provenance | [0x2e926654…f1c22667](https://explorer-studio.genlayer.com/tx/0x2e926654e20ddd483b94796209e80f3c84574d329ee394818f64af2cf1c22667) | FINALIZED / SUCCESS; 3 AGREE, 2 IDLE |

The evaluation has an agreeing leader and two successful agreeing independent validator executions. The two IDLE receipts explicitly say **“Validator execution cancelled after quorum”**, code `CONSENSUS_VALIDATOR_QUORUM_REACHED`. They did not vote against the verdict. This is a successful quorum result, not a claim of unanimous execution by all five selected validators. No mock web, mock LLM, leader-only mode or simulated transaction was used for the live evaluation.

Receipts preserve selected public RPC fields, vote maps, execution results, and equivalence outputs; duplicated source, simulator snapshots and provider configuration are omitted:

- [Deployment receipt](deployment-receipt.json)
- [Submission receipt](submission-receipt.json)
- [Evaluation receipt](evaluation-receipt.json)
- [Explorer screenshot: all three FINALIZED / SUCCESS](explorer-finalized.jpg)

## Locked claim and evidence

> Synthetic note version 2 derives from version 1, changing blue to green with the interval unchanged; history links both exact files. No external authorship or publication date is claimed.

The fixture consists of a 310-byte origin note, a 500-byte transition record and a 395-byte modified artifact (1,205 total). The transition record commits both exact note hashes and lengths and discloses the material color change. All files explicitly state their synthetic scope. The manifest's `timestamp: 1` values are equal synthetic chronology placeholders, **not claims that these files were published in 1970**. No external identity, trusted publication date or real-world origin is asserted.

| Role | Commit-pinned public evidence | SHA-256 |
| --- | --- | --- |
| Origin | [origin.txt](https://raw.githubusercontent.com/ANZA24k/TraceVerdict/485c93a3d29498d974a8219ba6e1aa25f8c30348/fixtures/origin.txt) | `2a9712e1bd9b959b3168e9b82a95d1b919559f138140d30f3794791c3f922edf` |
| History | [history.txt](https://raw.githubusercontent.com/ANZA24k/TraceVerdict/485c93a3d29498d974a8219ba6e1aa25f8c30348/fixtures/history.txt) | `803f26de6da1fafbd8e94d08103070d8fc12a68cf7e4e10ea61b2fa48548d0e9` |
| Artifact | [artifact.txt](https://raw.githubusercontent.com/ANZA24k/TraceVerdict/485c93a3d29498d974a8219ba6e1aa25f8c30348/fixtures/artifact.txt) | `def0c2d64838b8eb4c394b2dc4b46d654c0ca0588c5f2af158a6c011f5cf8105` |

[Exact submitted manifest](live-manifest.json). Manifest hash: `2c0b6182da62f1a937e10aadb64b48926b8fded21f910ecf26ee718c90d3cdba`.

## Finalized state and independent audit

Finalized state was read with Studio's **Finalized** state selector and independently through `genlayer-py` `read_contract(..., transaction_hash_variant=TransactionHashVariant.LATEST_FINAL)`.

| Field | Final value |
| --- | --- |
| Record ID | `1b8286a835249e0203642a416f256dd11b3806657e76f6e01934a3d50f001a17` |
| Application state | FINAL |
| Outcome | VERIFIED |
| Authentication | AUTHENTICATED for all three files |
| Origin / chain / modifications / support | SUPPORTED / SUPPORTED / SUPPORTED / SUPPORTED |
| Previous ID | Empty (initial claim) |
| Submitted at | `1792407288` (transaction time, Unix seconds) |
| Evaluated at | `1792407369` (transaction time, Unix seconds) |
| Decision hash | `b6d370223410d51975810a1a6824e26ad901881d753c158609943695754ca70f` |
| Counts | `{"final":1,"submitted":1}` |
| History | Exactly the record ID above, once |

Machine-readable [final record](final-record.json), [counts](final-counts.json) and [history](final-history.json) are preserved. Recomputed the decision hash using the full final record minus its hash, domain string and exact contract address; it matched.

```sh
python scripts/audit_record.py 0x454ca444D6BD8060DFD611F6CB26623ADa1DC363 docs/final-record.json
# FINAL VERIFIED decision_hash=b6d370223410d51975810a1a6824e26ad901881d753c158609943695754ca70f
```

## Validation

- Official GenVM linter 0.11.0: all 3 AST checks passed; SDK validation passed; TraceVerdict schema has 5 public methods (3 view, 2 write).
- Official genlayer-test 0.29.2 Direct Mode on Python 3.12: **61 passed**. Covers all dimension/outcome combinations, validator dissent/refetch, failed authentication, malformed model output, URL security, replay, revisions, deterministic timestamps/hashing and immutable final state.
- [Clean GitHub Actions run](https://github.com/ANZA24k/TraceVerdict/actions/runs/39240754150): **success**, including lint, SDK validation and all tests. An initial CI download failure was fixed by explicitly selecting stable GenVM v0.2.16 rather than a moving latest release candidate. The contract source was unchanged.
- One live semantic evaluation was run. PARTIAL, BROKEN_CHAIN and INCONCLUSIVE are covered by focused Direct Mode tests, not claimed as live demonstrations.

GenLayer is central because independent validators interpret provenance narratives and material modifications. SHA-256, URL/size/chronology checks and state transitions are deterministic; they cannot alone establish the semantic history judgment. This pilot verifies submitted synthetic document history, not universal authenticity or real-world authorship.
