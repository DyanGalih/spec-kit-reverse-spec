# Command Reference

## `/speckit.reverse-spec.scan`

### Purpose
Scan a source repository and identify candidate product features, source signals, and confidence labels.

### Required Inputs
- `--source <path-or-url>`

### Optional Inputs
- `--target <stack>`
- `--output <dir>`
- `--depth <n>`
- `--include-tests`
- `--include-docs`
- `--exclude <pattern>`

### Outputs
- `.reverse-spec/feature-inventory.md`
- `.reverse-spec/source-map.md`
- `.reverse-spec/assumptions.md`
- `.reverse-spec/scan-report.md`

### Recommended Next Command
- `/speckit.reverse-spec.extract`

## `/speckit.reverse-spec.extract`

### Purpose
Build draft reconstructed feature specification folders from source evidence and scan inventory.

### Required Inputs
- `--source <path-or-url>`
- `--target <stack>`

### Optional Inputs
- `--features <list|all>`
- `--max-features <n>`
- `--architecture-guard`
- `--security-review`
- `--memory-md`

### Outputs
- `specs/NNN-feature-name/spec.md`
- `specs/NNN-feature-name/reverse-analysis.md`
- `specs/NNN-feature-name/architecture-alignment.md`
- `specs/NNN-feature-name/security-considerations.md`
- `specs/NNN-feature-name/open-questions.md`
- `specs/NNN-feature-name/source-traceability.md`
- `.reverse-spec/extraction-report.md`

### Recommended Next Command
- `/speckit.reverse-spec.map`

## `/speckit.reverse-spec.map`

### Purpose
Map extracted features to the target architecture and constitution, then record drift and required refactors.

### Required Inputs
- `--target <stack>`

### Optional Inputs
- `--constitution <path>`
- `--source <path-or-url>`
- `--features <list|all>`

### Outputs
- `specs/NNN-feature-name/architecture-alignment.md`

### Recommended Next Command
- `/speckit.reverse-spec.validate`

## `/speckit.reverse-spec.validate`

### Purpose
Validate generated feature folders for completeness, traceability, architecture readiness, and security readiness.

### Required Inputs
- `$ARGUMENTS` conceptually

### Optional Inputs
- `--mode <draft|review-ready|strict>`
- `--stop-on-blockers <true|false>`
- `--features <list|all>`

### Outputs
- `.reverse-spec/validation-report.md`

### Recommended Next Command
- `/speckit.reverse-spec.export`

## `/speckit.reverse-spec.export`

### Purpose
Finalize draft reconstructed specs, stabilize filenames, and write handoff reports.

### Required Inputs
- `--source <path-or-url>`
- `--target <stack>`

### Optional Inputs
- `--features <list|all>`
- `--output <dir>`

### Outputs
- `.reverse-spec/export-report.md`
- `.reverse-spec/pipeline-report.md`

### Recommended Next Command
- `/speckit.architecture-guard.architecture-review`

## `/speckit.reverse-spec.full-pipeline`

### Purpose
Run the full reverse-spec workflow from scratch, orchestrating scan, extract, map, validate, and export without bypassing human review gates.

### Required Inputs
- `--source <path-or-url>`
- `--target <stack>`

### Optional Inputs
- `--output <dir>`
- `--features <list|all>`
- `--max-features <n>`
- `--memory-md <true|false>`
- `--architecture-guard <true|false>`
- `--security-review <true|false>`
- `--constitution <path>`
- `--mode <draft|review-ready|strict>`
- `--stop-on-blockers <true|false>`

### Outputs
- `.reverse-spec/feature-inventory.md`
- `.reverse-spec/source-map.md`
- `.reverse-spec/assumptions.md`
- `.reverse-spec/scan-report.md`
- `.reverse-spec/extraction-report.md`
- `.reverse-spec/validation-report.md`
- `.reverse-spec/export-report.md`
- `.reverse-spec/pipeline-report.md`

### Recommended Next Command
- `/speckit.memory-md.plan-with-memory`

## Example Invocation Pattern

Every command accepts `$ARGUMENTS` conceptually. A typical pattern is:

```text
/speckit.reverse-spec.scan $ARGUMENTS --source ./legacy-app --output .reverse-spec
```
