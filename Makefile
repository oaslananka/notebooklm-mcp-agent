.PHONY: setup lint format typecheck test test-unit test-integration test-e2e build docs docs-serve security sbom catalog verify-structure verify-docs verify-owner verify-release gc verify clean

setup:
	task setup

lint:
	task lint

format:
	task format

typecheck:
	task typecheck

test:
	task test

test-unit:
	task test:unit

test-integration:
	task test:integration

test-e2e:
	task test:e2e

build:
	task build

docs:
	task docs

docs-serve:
	task docs:serve

security:
	task security

sbom:
	task sbom

catalog:
	task catalog

verify-structure:
	task verify:structure

verify-docs:
	task verify:docs

verify-owner:
	task verify:owner

verify-release:
	task verify:release

gc:
	task gc

verify:
	task verify

clean:
	task clean
