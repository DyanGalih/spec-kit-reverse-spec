---
description: "Extract draft reconstructed feature specifications from source behavior and scan evidence."
---

# Command: /speckit.reverse-spec.extract

## Purpose
Convert discovered source behavior into draft Spec Kit-compatible feature specification folders that describe what the rebuilt system must do, not how the original code does it.

## User Input
Use `$ARGUMENTS` to provide the source, target, feature scope, and optional integration toggles.

Required:
- `--source <path-or-url>`
- `--target <stack>`

Optional:
- `--features <list|all>`
- `--max-features <n>`
- `--architecture-guard`
- `--security-review`
- `--memory-md`

## Preconditions
- `--source` and `--target` are both provided.
- `.reverse-spec/feature-inventory.md` is available or can be generated inline from source evidence.
- The `specs/` output path is writable.

## Procedure
1. Parse `$ARGUMENTS` conceptually and resolve the feature scope, feature cap, and integration flags.
2. Read `.reverse-spec/feature-inventory.md` when present to reuse scan results.
3. If scan output is missing, perform the scan behavior inline before extraction continues.
4. For each selected feature, create `specs/NNN-feature-name/` with stable numbering and stable filenames.
5. Generate:
   - `spec.md`
   - `reverse-analysis.md`
   - `architecture-alignment.md`
   - `security-considerations.md`
   - `open-questions.md`
   - `source-traceability.md`
6. Write the spec as a draft reconstructed specification that states the behavior the rebuilt system must implement.
7. Preserve traceability to source files, tests, and docs while avoiding implementation bias.

## Outputs
Produce feature folders under `specs/` and refresh any supporting reverse-spec artifacts required for downstream map, validate, and export steps.

## Failure Handling
- Stop when `--source` or `--target` is missing.
- Reduce scope when `--max-features` is reached.
- Classify uncertain behavior as an open question instead of turning it into a requirement.
- Record missing evidence in reverse-analysis and source-traceability artifacts.

## Quality Checklist
- Each selected feature has a numbered folder.
- Every folder contains the required files.
- Specs describe required behavior, not original implementation mechanics.
- Traceability links behavior back to source evidence.
- Open questions are captured explicitly.

## Example Usage
```text
/speckit.reverse-spec.extract $ARGUMENTS --source ./legacy-app --target "React + Node" --features auth,billing --max-features 5 --architecture-guard --security-review --memory-md
```

## Next Recommended Commands
- `/speckit.reverse-spec.map $ARGUMENTS`
- `/speckit.reverse-spec.validate $ARGUMENTS`
