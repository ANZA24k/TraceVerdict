# Security model

## Boundaries

All submitted claims, chronology, manifest labels and fetched text are untrusted. Evidence is JSON-encoded in one explicit untrusted-data section after a fixed rubric. There is no tool-enabled browsing by the model and no execution of downloaded data. Only submitted URLs are fetched. The fixed rubric forbids embedded instructions, outside facts and self-assertion as independent proof. Malformed or oversized model responses become UNKNOWN; authentication failure bypasses the model and yields INCONCLUSIVE.

The leader and validators each retrieve every file, verify length/SHA-256, parse UTF-8, rerun the task and compare the entire normalized result. No leader-only rationale enters persistent state. A correctly formatted leader result alone is insufficient. Transport and model availability can prevent consensus or produce a conservative final INCONCLUSIVE.

HTTPS host/path restrictions reduce SSRF and mutable-reference risk. The GenVM web service owns DNS, TLS, redirect and response download behavior. The SDK has no per-request streaming/redirect/maximum-response option: application checks happen after retrieval, so declared size limits bound accepted evidence and prompt size, not the service's initial download. Platform isolation and transport limits remain necessary.

## Deterministic safeguards

- Closed JSON schemas; duplicate keys rejected; bounded manifests, claims, files and pagination.
- Integer timestamps pinned to transaction time; claimed evidence dates cannot be future or out of order. They are not publication attestations.
- Commit pins plus exact content commitments; duplicate URLs/hashes rejected.
- Replay commitments bind canonical claim+manifest; record IDs bind caller and contract.
- Caller ownership applies to revision links; anyone may settle a pending record under its locked input.
- A follow-up requires a new evidence hash, retains the same owner and links a final predecessor. Metadata-only retries cannot bypass that restriction.
- Evaluation performs no external stateful calls; the entire state update is after consensus. Final records cannot be reevaluated, deleted or overwritten. No upgrade/admin/value-transfer methods exist.
- Decision hashes bind all final fields, with domain separation and deterministic encoding.

## Limits and residual risks

This is a provenance-evidence assessment, not a cryptographic certificate of real-world origin, identity, ownership or trusted time. SHA-256 and a Git commit pin cannot establish honest authorship, publication time or completeness. Submit signed source records or independently corroborated records when those claims matter. This v1 interprets such records as text and does not implement cryptographic signature verification.

Prompt injection, shared model error, colluding validators, curated/false evidence, Git hosting compromise and evidence unavailability remain risks. Delimiting data and independent consensus reduce risk, not eliminate it. No internet-wide search for omitted evidence occurs. Agreement is exact across four categorical judgments; ambiguous sources can cause dissent and protocol non-resolution. A finalized INCONCLUSIVE is immutable; a follow-up requires new evidence. Pending records do not expire, and this contract has no asset settlement or financial incentive mechanism.

Identical claim+manifest submissions are globally deduplicated, so another caller may submit public material first. Submission ownership describes the on-chain record owner, never an assertion of artifact ownership. Textual variations are separate claims. There is no curated registry or resource cap across all callers; normal chain admission/fees govern storage abuse.

## Reporting

Report reproducible defects through this repository's GitHub security reporting when available. If private reporting is unavailable, contact the repository maintainer before publishing exploitation details. Do not place private documents, personal information, credentials or confidential artifacts in public evidence.
