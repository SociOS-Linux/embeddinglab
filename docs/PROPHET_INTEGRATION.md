# EmbeddingLab — Prophet integration

How this lab hands off to the wider SocioProphet estate. All handoff targets are declared
in [`../lab.manifest.json`](../lab.manifest.json) under `governanceHandoff` and in the
service manifest `governance` / `sourceosCarry` blocks.

| Target | Relationship |
|--------|--------------|
| `SocioProphet/holmes` | consumes the embedding/rerank surface as a product capability |
| `SocioProphet/model-router` | routes to the governed surface |
| `SocioProphet/model-governance-ledger` | receives promotion evidence (evals, provenance) |
| `SocioProphet/guardrail-fabric` | enforces guardrail policies on the surface |
| `SocioProphet/functional-model-surfaces` | canonical schema authority for the manifest |
| `SourceOS-Linux/sourceos-model-carry` | disabled-by-default SourceOS carry reference |

## Governance handoff

- `governance.ledgerRequired` / `guardrailRequired` / `routingRequired` are all `true` in
  the service manifest — the surface cannot be promoted without ledger evidence, guardrail
  policy, and a routing entry.
- `sourceosCarry.carriesMutableModelState` is `false` and `clientRefRequired` is `true`:
  SourceOS carries only a signed client reference, never mutable model state.
