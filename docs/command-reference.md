# Command Reference

## `/speckit.reverse-spec.scan`

Scans source code, routes, tests, docs, and related structure to identify candidate product features and produce the first reverse-spec artifacts.

## `/speckit.reverse-spec.extract`

Builds `specs/NNN-feature-name/` folders from source evidence and writes draft reconstructed specifications.

## `/speckit.reverse-spec.map`

Places each extracted feature in the target stack, identifies drift, and records architecture boundaries.

## `/speckit.reverse-spec.validate`

Checks required files and content, then assigns a readiness status for each feature folder.

## `/speckit.reverse-spec.export`

Finalizes filenames and writes export and pipeline reports for handoff.

## `/speckit.reverse-spec.full-pipeline`

Runs scan, extract, map, validate, and export in order while keeping review gates visible.

## Example Invocation Pattern

Every command accepts `$ARGUMENTS` conceptually. A typical pattern is:

```text
/speckit.reverse-spec.scan $ARGUMENTS --source ./legacy-app --output .reverse-spec
```
