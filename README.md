# TraceVerdict

**Consensus judgments for the provenance and modification history of public artifacts.**

TraceVerdict is a standalone GenLayer Intelligent Contract. Submit a precise artifact-history claim and a locked manifest of public, commit-pinned UTF-8 evidence. GenLayer leaders and validators independently retrieve the files, authenticate their exact SHA-256 and byte length, and assess origin, chain completeness, modification disclosure and claim support. Deterministic rules derive `VERIFIED`, `PARTIAL`, `BROKEN_CHAIN` or `INCONCLUSIVE`.

No frontend, wallet integration, escrow, external oracle, database or administrator is required.

**Live on stable Studionet:** [contract](https://explorer-studio.genlayer.com/address/0x454ca444D6BD8060DFD611F6CB26623ADa1DC363). A real Full Consensus evaluation finalized **VERIFIED**. [Complete evidence and reproducible decision hash](docs/LIVE_VERIFICATION.md) · [Submission text](docs/SUBMISSION.md).

## Workflow

1. `submit(claim, evidence_manifest, previous_id)` commits the claim and manifest, records caller ownership and transaction time, and returns a content-derived record ID. Use `""` for a new claim.
2. Anyone calls `evaluate(record_id)`. Validators **re-fetch all evidence and independently rerun the assessment**. The complete normalized authentication vector, four ratings and derived outcome must match the leader. Disagreement follows the protocol's consensus/rotation behavior; a failed transaction does not finalize a verdict.
3. Successful evaluation atomically appends the ID to history and makes the record `FINAL`. No method edits or deletes a final verdict.
4. The prior owner can submit a follow-up using `previous_id`, with at least one new evidence content hash. The original record remains immutable; branches are allowed and do not supersede older records.

`get_record(id)` returns canonical JSON. `get_counts()` returns submission/final counts. `get_history(offset, limit)` returns final IDs in evaluation order, up to 50 per page.

## Decision rules

Each dimension is `SUPPORTED`, `MISSING`, `CONTRADICTED` or `UNKNOWN`.

| Condition | Outcome |
| --- | --- |
| Any file unavailable, not valid UTF-8, wrong size or wrong hash | INCONCLUSIVE; model not called |
| All files authenticated; any dimension CONTRADICTED | BROKEN_CHAIN |
| Otherwise any dimension UNKNOWN | INCONCLUSIVE |
| Otherwise any dimension MISSING | PARTIAL |
| All four dimensions SUPPORTED | VERIFIED |

Authentication means the submitted bytes match, **not** that their statements are true. A known gap differs from a contradiction. An inaccessible source does not prove misconduct. The model must not accept a commit pin as proof of authorship, a self-asserted date as an authenticated timestamp, or a document's instruction as evidence. The synthetic fixture has deliberately narrow internal-history scope.

## Manifest

The argument is a JSON array (not a URL to a mutable manifest). Each entry has exactly:

```json
{"url":"https://raw.githubusercontent.com/owner/repo/0123456789abcdef0123456789abcdef01234567/path.txt","sha256":"64 lowercase hexadecimal characters","bytes":123,"timestamp":1,"role":"artifact"}
```

The example is schema-only, not a live evidence URL. Use the actual fixture manifest linked from [live verification](docs/LIVE_VERIFICATION.md).

Limits: 1–6 unique URLs and content hashes; 8,192 bytes/file; 24,576 bytes total; manifest at most 6,000 UTF-8 bytes; claim 20–2,000 UTF-8 bytes, with no surrounding whitespace. The last entry identifies the artifact. Roles are `origin`, `history`, `artifact`. Entries have positive, nondecreasing integer timestamps no later than the submission transaction time. These are **claimed chronology metadata**, not independent attestations. The model assesses date claims when they are material. No floats or booleans are accepted as timestamps/lengths.

Only exact HTTPS raw GitHub file URLs with a 40-character lowercase commit SHA are supported. No mutable refs, arbitrary hosts, credentials, port overrides, query strings, fragments, escapes, empty/dot path segments or rendered HTML. URLs are references; SHA-256 is the authoritative content commitment. Redirect handling is platform-controlled; a non-200 response is unavailable, and any returned bytes still must pass the commitment checks. This version intentionally excludes binary release downloads and general websites.

## Replay, ownership and hashing

Canonical JSON uses sorted keys, ASCII escapes and separators `(',', ':')`. SHA-256 hashes UTF-8 bytes of that encoding. Duplicate JSON keys are rejected before canonicalization. Global replay protection rejects an identical canonical claim/manifest pair even under another caller or JSON key order. Semantically similar but textually different claims are not deduplicated. Record IDs bind the contract address, owner and commitment. Only the prior owner may link a follow-up; evaluation is permissionless.

`decision_hash = SHA256(canonical({"domain":"TraceVerdict/decision/v1","contract":address,"record":final_record_without_decision_hash}))`.

The digest binds the full locked input, parent ID, owner, transaction times, authentication, ratings and outcome. It is contract-address scoped; network identity is supplied by the deployment record. Application `FINAL` is irreversible through this contract's methods; always wait for **protocol transaction finalization** before relying on a receipt.

## Tests

Python 3.12+:

```sh
python -m pip install -r requirements-dev.txt
genvm-lint check contracts/traceverdict.py
python -m pytest -q
```

Tests use the official `genlayer-test` Direct Mode, including independent validator agreement/dissent, changed remote bytes, all outcome dimensions, integrity failures, URL restrictions, replay, revision ownership, final immutability and decision-hash recomputation. Direct Mode mocks are not a substitute for multi-validator network execution. The suite double-encodes mock LLM strings because genlayer-test 0.29.2 auto-parses JSON mocks even for text responses; the deployed contract uses text mode and its own duplicate-rejecting parser. The injection test verifies data separation and conservative plumbing with a controlled model response, not universal prompt-injection resistance.

See [deployment](DEPLOYMENT.md), [security](SECURITY.md), [API sources](docs/API_SOURCES.md) and [live evidence](docs/LIVE_VERIFICATION.md).

## Why GenLayer is central

Hashes can establish byte identity; they cannot establish whether a provenance narrative is supported, whether a modification is material, or whether the chain omits a meaningful transition. GenLayer validators independently make those qualitative judgments from public evidence, and consensus controls the on-chain verdict. Conventional deterministic checks protect the inputs and state transitions around that judgment.
