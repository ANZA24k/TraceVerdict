# Official API review — 2026-10-19

Reviewed before implementation:

- [Equivalence Principle](https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle): independent evidence verification; custom `gl.vm.run_nondet_unsafe(leader, validator)`; `gl.vm.Return` and `.calldata`; full normalized decision comparison.
- [Web access](https://docs.genlayer.com/developers/intelligent-contracts/features/web-access): `gl.nondet.web.get` in nondeterministic execution, independent web retrieval. Actual pinned SDK uses `.status`, `.body` and `.headers`.
- [Transaction context](https://docs.genlayer.com/developers/intelligent-contracts/features/transaction-context): caller/contract addresses; transaction-pinned `datetime.now(timezone.utc)` and integer Unix seconds.
- [Direct Mode](https://docs.genlayer.com/api-references/genlayer-test/direct): `direct_vm`, `direct_deploy`, mocks, `prank`, `warp`, `run_validator`.
- [GenVM linter](https://docs.genlayer.com/api-references/genlayer-linter): `genvm-lint check` combines AST checks with exact-SDK validation/schema extraction.
- [Networks](https://docs.genlayer.com/developers/networks): stable Studionet RPC/chain ID 61999; Studio-dev preview is a different network, 61997.
- [Studio](https://docs.genlayer.com/developers/intelligent-contracts/tools/genlayer-studio) and [deployment](https://docs.genlayer.com/developers/intelligent-contracts/deploying): built-in tooling, network choice and verification of execution outcome separately from lifecycle status.

The contract uses only the public SDK surface and standard-library deterministic parsing/hash operations. No internal prompt templates, deprecated `gl.exec_prompt`, external wall clock, arbitrary-host web oracle or leader-only validator is used.
