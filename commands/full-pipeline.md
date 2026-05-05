---
description: "Orchestrate the reverse-spec workflow from preflight through export without autopiloting implementation."
---

# Command: /speckit.reverse-spec.full-pipeline

## Purpose
Coordinate scan, extract, map, validate, and export in a governed sequence that preserves review gates and avoids auto-implementation.

## User Input
Use `$ARGUMENTS` to supply the source repository, target stack, output directory, feature scope, and pipeline mode.

Required:
- `--source <path-or-url>`

Required unless explicitly auto-detectable:
- `--target <stack>`

Optional:
- `--output <dir>` default `.reverse-spec`
- `--features <list|all>` default `all`
- `--max-features <n>`
- `--memory-md <true|false>` default `true`
- `--architecture-guard <true|false>` default `true`
- `--security-review <true|false>` default `true`
- `--constitution <path>` default `architecture_constitution.md`
- `--mode <draft|review-ready|strict>`
- `--stop-on-blockers <true|false>` default `true`

## Preconditions
- The source repository is available.
- The pipeline can read or infer the target stack when allowed.
- The output directory is writable.
- Optional integrations may or may not be installed, but missing ones must not break orchestration.

## Procedure
1. Parse `$ARGUMENTS` conceptually and resolve source, target, scope, mode, and integration toggles.
2. Preflight the repository, target stack, constitution file, and optional integrations.
3. If `--memory-md true`, recommend memory context before the scan begins.
4. Run scan behavior and write the reverse-spec inventory artifacts.
5. Run extract behavior and generate draft reconstructed feature specs.
6. Run map behavior and produce architecture alignment per feature.
7. Prepare for security review, but do not auto-run implementation or auto-run `speckit.security-review.branch`.
8. Run validate behavior and classify readiness.
9. Run export behavior and write the final pipeline reports.
10. Print quality gates and the exact next commands without pretending the generated specs are final truth.

## Pipeline
A. Preflight
B. Optional memory-md context recommendation
C. Scan
D. Extract
E. Map
F. Security preparation
G. Validate
H. Export
I. Print quality gates

## Outputs
Produce the same outputs as the scan, extract, map, validate, and export commands, plus a complete `.reverse-spec/pipeline-report.md`.

## Failure Handling
- Stop on blockers when `--stop-on-blockers true`.
- Do not auto-fix architecture issues.
- Do not auto-run implementation.
- Do not auto-run `speckit.security-review.branch`.
- Do not preserve source architecture blindly.

## Quality Checklist
- The workflow is orchestrated rather than autopiloted.
- Review gates remain visible.
- Draft status is preserved throughout the pipeline.
- Optional integrations are recommended, not forced.

## Example Usage
```text
/speckit.reverse-spec.full-pipeline $ARGUMENTS --source ./legacy-app --target "Next.js + PostgreSQL" --output .reverse-spec --features all --mode review-ready --stop-on-blockers true
```

## Next Recommended Commands
- `/speckit.memory-md.plan-with-memory`
- `/speckit.reverse-spec.full-pipeline --source <repo> --target "<stack>"`
- `/speckit.memory-md.capture`
- `/speckit.architecture-guard.architecture-review`
- `/speckit.security-review.audit`
- `/speckit.plan`
- `/speckit.tasks`
- `/speckit.implementation`
- `/speckit.security-review.branch`
- `/speckit.memory-md.capture-from-diff`
