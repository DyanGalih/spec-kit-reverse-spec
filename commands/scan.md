---
description: "Scan a source repository, classify product features, and generate the reverse-spec inventory."
---

# Command: /speckit.reverse-spec.scan

## Purpose
Scan a source OSS repository and produce the first-pass feature inventory, source map, assumptions log, and scan report that downstream commands will refine.

## User Input
Use `$ARGUMENTS` to supply the source repository and optional scope filters.

Required:
- `--source <path-or-url>`

Optional:
- `--target <stack>`
- `--output <dir>`
- `--depth <n>`
- `--include-tests`
- `--include-docs`
- `--exclude <pattern>`

## Preconditions
- The source repository exists and can be read.
- `--source` is provided explicitly.
- The output directory is writable.

## Procedure
1. Parse `$ARGUMENTS` conceptually and resolve the source repository, target stack, output directory, depth, inclusion flags, and exclusion rules.
2. Traverse the repository with the requested depth and collect candidate signals from routes, controllers, pages, components, models, migrations, API endpoints, CLI commands, jobs/workers, events/listeners, services, tests, and docs/examples.
3. Separate product features from infrastructure helpers, build-system files, and purely operational plumbing.
4. Group signals into candidate features and assign confidence:
   - `HIGH` when routes, tests, and docs or source comments agree.
   - `MEDIUM` when source and routes agree but tests or docs are missing.
   - `LOW` when the feature is inferred from source structure only.
5. Record source paths, entry points, and observed behavior without rewriting the implementation as the spec.
6. Write the scan outputs into `$ARGUMENTS`-controlled output directory, defaulting to `.reverse-spec`.

## Outputs
Produce:
- `.reverse-spec/feature-inventory.md`
- `.reverse-spec/source-map.md`
- `.reverse-spec/assumptions.md`
- `.reverse-spec/scan-report.md`

## Failure Handling
- Stop if `--source` is missing.
- Report unreadable paths, permission issues, or exclusion rules that remove all meaningful source files.
- Mark features as low confidence when evidence is sparse instead of guessing.

## Quality Checklist
- Source path was explicit.
- Feature candidates are separated from infrastructure helpers.
- Confidence labels are present for each feature.
- Outputs were written to the configured work directory.
- Assumptions were captured separately from evidence.

## Example Usage
```text
/speckit.reverse-spec.scan $ARGUMENTS --source ./legacy-app --target "NestJS + PostgreSQL" --output .reverse-spec --depth 4 --include-tests --include-docs
```

## Next Recommended Commands
- `/speckit.reverse-spec.extract $ARGUMENTS`
- `/speckit.memory-md.plan-with-memory` if memory-md is available
