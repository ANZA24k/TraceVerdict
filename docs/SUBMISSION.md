# GenLayer Intelligent Contracts submission

## Project

TraceVerdict

## One-line description

A GenLayer Intelligent Contract that verifies public artifact provenance and disclosed modification history through independent validator consensus.

## Longer description

TraceVerdict locks a precise artifact-history claim and an immutable manifest of commit-pinned public evidence. GenLayer leaders and validators independently retrieve and authenticate exact file bytes, then judge origin, provenance-chain completeness, material-change disclosure and claim support. Deterministic rules derive VERIFIED, PARTIAL, BROKEN_CHAIN or INCONCLUSIVE, while enforcing limits, chronology, replay protection, revision ownership and irreversible final records. Every decision is bound to a reproducible SHA-256 digest and appended to public history. The live demonstration verifies the internal history of explicitly synthetic notes; it does not certify real-world authorship or publication time.

## Recommended tags

Intelligent Contracts; Provenance; Data Integrity; Verification; AI Consensus. Choose the closest labels available in the portal.

## Notes / Description (905 characters)

TraceVerdict is a standalone GenLayer Intelligent Contract for provenance and modification-history verification. Submitters lock a claim and commit-pinned public evidence manifest with SHA-256 and exact byte lengths. Leaders and validators independently re-fetch, authenticate and assess origin, chain completeness, disclosed modifications and claim support. Deterministic rules derive VERIFIED, PARTIAL, BROKEN_CHAIN or INCONCLUSIVE. Safeguards include strict HTTPS URL validation, bounded evidence, replay protection, owner-authorized revision links, transaction timestamps, immutable final records, append-only history and a deterministic decision hash. The exact committed source is deployed on stable Studionet. A real Full Consensus synthetic-history test finalized VERIFIED with authenticated evidence. Includes 61 passing Direct Mode tests, GenVM lint/SDK validation, green CI and public receipts.

## Evidence

See [live verification](LIVE_VERIFICATION.md) for contract, deployment, submission and evaluation links, source commit/hash, fixture manifest, outcome and final state.
