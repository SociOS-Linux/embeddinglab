# EmbeddingLab — lab surface

`embeddinglab` is a **lab-only** workspace: it emits governed functional-service
manifests and evaluation evidence for downstream SocioProphet services. It does not
self-promote models into production and does not carry mutable model state into SourceOS.

## Surfaces

Enumerated in [`../lab.manifest.json`](../lab.manifest.json):

- embeddings
- rerankers
- hybrid-retrieval-preparation
- vector-evaluation
- semantic-indexing

## Service manifest

The primary functional surface is declared in
[`../service-manifest/functional-service.v1.json`](../service-manifest/functional-service.v1.json),
which conforms to the canonical `functional-service.v1` schema
(`SocioProphet/functional-model-surfaces`). Inputs, outputs, evals, governance flags, and
the SourceOS carry policy are all declared there.

## Evidence

- Deterministic offline smoke: `make smoke` (the M2 promotion gate).
- Maturity record: [`../repo.maturity.yaml`](../repo.maturity.yaml) (`repo-maturity.v1`).
- Promotion dry-run gate: `make release-dry-run` (validate + smoke + carry).

## Boundary

Lab-only. No model weights, datasets, secrets, or credentials are committed. Scaffolding
directories (`datasets/`, `evals/`, `adapters/`, `training-runs/`) hold **references and
provenance only**.
