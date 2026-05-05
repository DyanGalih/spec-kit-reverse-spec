---
description: "Finalize reverse-engineered specs and generate export and pipeline reports."
---

# Command: /speckit.reverse-spec.export

## Purpose
Finalize the reconstructed specification folders, stabilize filenames, and generate the release-facing reverse-spec reports.

## User Input
Use `$ARGUMENTS` to supply the source, target, and export scope that should be finalized.

Required:
- `--source <path-or-url>`
- `--target <stack>`

Optional:
- `--features <list|all>`
- `--output <dir>`

## Preconditions
- Feature folders already exist or can be derived from the reverse-spec pipeline.
- Validation has been run or equivalent checks are available.
- The output directory is writable.

## Procedure
1. Parse `$ARGUMENTS` conceptually and resolve source, target, output, and feature scope.
2. Finalize `specs/NNN-feature-name/` folders without changing their meaning.
3. Ensure every spec clearly states that it is a draft reconstructed from source behavior.
4. Stabilize filenames so they remain consistent across export runs.
5. Generate:
   - `.reverse-spec/export-report.md`
   - `.reverse-spec/pipeline-report.md`
6. Print the exact next commands required for the delivery workflow.

## Outputs
Produce:
- `.reverse-spec/export-report.md`
- `.reverse-spec/pipeline-report.md`

## Failure Handling
- Stop if `--source` or `--target` is missing.
- Do not rename feature folders in a way that breaks traceability.
- Preserve draft status even when the export is clean.

## Quality Checklist
- Specs remain explicitly draft reconstructed artifacts.
- Filenames are stable.
- Export and pipeline reports exist.
- Next commands are printed exactly as documented.

## Example Usage
```text
/speckit.reverse-spec.export $ARGUMENTS --source ./legacy-app --target "NestJS + PostgreSQL" --features all --output .reverse-spec
```

## Next Recommended Commands
- `/speckit.memory-md.capture`
- `/speckit.architecture-guard.architecture-review`
- `/speckit.security-review.audit`
- `/speckit.plan`
- `/speckit.tasks`
- `/speckit.implementation`
- `/speckit.security-review.branch`
- `/speckit.memory-md.capture-from-diff`
