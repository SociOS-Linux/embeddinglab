.PHONY: validate validate-spine validate-negative smoke carry emit-service-manifest release-dry-run

validate: validate-spine
	python3 tools/validate.py

emit-service-manifest:
	cat service-manifest/functional-service.v1.json

release-dry-run: validate smoke carry
	@echo "release-dry-run OK: manifest + maturity spine validated, offline smoke passed, SourceOS carry emitted (disabled-by-default)."

validate-spine:
	python3 tools/validate_spine.py

smoke:
	python3 tools/smoke.py

carry:
	python3 tools/emit_sourceos_carry.py > examples/sourceos-carry.embeddinglab.json

validate-negative:
	python3 tools/run_negative_fixtures.py
