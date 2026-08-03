#!/usr/bin/env python3
import json, sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
s=json.load(open(R/"schemas/crossmodal-embedding.schema.json"))
ex=json.load(open(R/"examples/crossmodal-query.example.json"))
try:
    from jsonschema import Draft202012Validator as V
    errs=list(V(s).iter_errors(ex))
    if errs: print("FAIL:", errs[0].message); sys.exit(1)
except ImportError:
    pass
# teeth: shared space required; combined mode must carry both modalities; results labelled by modality
assert ex["unified_space_ref"], "no shared vector space"
if ex["query"]["mode"]=="combined":
    assert ex["query"].get("text") and ex["query"].get("image_ref"), "combined must carry text+image"
assert all(r["modality"] in ("text","image") for r in ex["results"]), "results must be modality-labelled"
# adversarial: image-mode query without image_ref must be schema-invalid
try:
    from jsonschema import Draft202012Validator as V
    bad={"query":{"mode":"image"},"unified_space_ref":"x","results":[]}
    assert list(V(s).iter_errors(bad)), "teeth: image mode without image_ref must be rejected"
except ImportError:
    pass
print("OK: crossmodal-embedding contract validates (shared space + modality teeth)")
