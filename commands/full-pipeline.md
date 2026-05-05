---
description: "Orchestrate the complete reverse-spec workflow from preflight through export."
---

# Command: /speckit.reverse-spec.full-pipeline

## Purpose

Coordinate scan, extract, map, validate, and export in a governed sequence. Preserves review gates and avoids auto-autopiloting implementation decisions. Orchestrates the entire reverse-spec workflow while maintaining explicit control points for team review.

The pipeline is a **guide, not an autopilot**. It surfaces decisions, respects blockers, and prints next steps without pretending generated specs are final truth.

## User Input ($ARGUMENTS)

Use `$ARGUMENTS` to provide the source repository, target stack, and pipeline configuration.

**Required:**
- `--source <path-or-url>` — Source repository to reverse-engineer

**Required unless explicitly auto-detectable:**
- `--target <stack>` — Target technology stack (e.g., "NestJS + PostgreSQL")

**Optional:**
- `--output <dir>` — Output directory for all reverse-spec artifacts; default `.reverse-spec`
- `--features <list|all>` — Features to process; default `all`
- `--max-features <n>` — Cap on number of features; default `0` (unlimited)
- `--memory-md <true|false>` — Recommend memory context before scan; default `true`
- `--architecture-guard <true|false>` — Enable architecture cross-checks; default `true`
- `--security-review <true|false>` — Enable security considerations output; default `true`
- `--constitution <path>` — Architecture constitution file; default `architecture_constitution.md`
- `--mode <draft|review-ready|strict>` — Validation strictness; default `review-ready`
- `--stop-on-blockers <true|false>` — Exit on blocking issues; default `true`

## Preconditions

- The source repository is accessible (local path or cloneable).
- The target stack is known or can be auto-detected from the repository.
- The output directory is writable (will be created if missing).
- Optional companion extensions (memory-md, architecture-guard, security-review) may or may not be installed.

## Procedure

### Phase A: Preflight

1. Validate `--source` is provided and accessible.
2. Validate or auto-detect `--target` stack.
3. Resolve `--output` directory; create if missing.
4. Check for optional integrations (memory-md, architecture-guard, security-review).
5. Load `--constitution` file if it exists; warn if missing.
6. Print preflight summary.

### Phase B: Optional Memory Context Recommendation

7. If `--memory-md true`, check if memory context exists and recommend reviewing.

### Phase C: Scan

8. Run scan behavior: collect signals, separate features from infrastructure, assign confidence, record assumptions.

### Phase D: Extract

9. Run extract behavior: create spec folders, populate templates with requirements, traceability, architecture, security, questions.

### Phase E: Map

10. Run map behavior: map source to target architecture, document boundaries, identify drift, record refactor prerequisites.

### Phase F: Security Preparation

11. Prepare for security review (do NOT auto-run): confirm security-considerations.md exists, note high-security features.

### Phase G: Validate

12. Run validate behavior: check files and content, assign readiness status per feature, handle blockers per `--stop-on-blockers`.

### Phase H: Export

13. Run export behavior: finalize folders, mark as draft, generate export and pipeline reports.

### Phase I: Print Quality Gates and Next Commands

14. Print exact next steps to console with copy-paste-ready commands.

## Pipeline Phases (Reference)

| Phase | Step | Output | Next |
|-------|------|--------|------|
| **A** | Preflight | Summary | Continue or abort |
| **B** | Memory recommendation | Context note | Continue |
| **C** | Scan | Feature inventory | Extract |
| **D** | Extract | Spec folders | Map |
| **E** | Map | Architecture alignment | Security prep |
| **F** | Security preparation | Security review note | Validate |
| **G** | Validate | Validation report | Export or pause for decisions |
| **H** | Export | Export + pipeline reports | Review gates and next commands |
| **I** | Print quality gates | Console output (next steps) | Human decision |

## Outputs

**Reverse-Spec Artifacts** (`.reverse-spec/`):
- `feature-inventory.md` (from scan)
- `source-map.md` (from scan)
- `assumptions.md` (from scan)
- `scan-report.md` (from scan)
- `extraction-report.md` (from extract)
- `architecture-report.md` (from map)
- `validation-report.md` (from validate)
- `export-report.md` (from export)
- `pipeline-report.md` (from export)

**Spec Folders** (`specs/NNN-feature-name/`):
- All 6 template files per feature (spec.md, reverse-analysis.md, architecture-alignment.md, security-considerations.md, open-questions.md, source-traceability.md)

**Console Output**:
- Exact next-step commands ready for copy-paste

## Failure Handling

- **Missing `--source`**: Stop immediately with error.
- **Unknown `--target`**: Warn; require explicit `--target` specification or pause for user input.
- **Constitution file missing**: Warn; use default target-stack rules; continue.
- **Blocking issues in validate**: If `--stop-on-blockers true`, pause; print blocker summary; require manual approval to continue.
- **Missing integrations**: If memory-md, architecture-guard, or security-review are unavailable, note them as optional; continue without auto-run.
- **Extraction fails**: Report which step failed; suggest manual run of that command for debugging.

## Quality Checklist

- [ ] `--source` was provided explicitly.
- [ ] `--target` was provided or auto-detected; no ambiguity.
- [ ] Preflight completed without errors.
- [ ] All nine pipeline phases completed successfully.
- [ ] All scan, extract, map, validate, and export artifacts exist.
- [ ] Spec folders are numbered stably (001, 002, ...).
- [ ] All specs are marked as DRAFT reconstructed.
- [ ] Open blocking questions are visible and summarized.
- [ ] Next-step commands are printed to console.
- [ ] Pipeline is orchestrated, not autopiloted.

## Example Usage

```text
/speckit.reverse-spec.full-pipeline $ARGUMENTS \
  --source ./legacy-app \
  --target "NestJS + PostgreSQL" \
  --output .reverse-spec \
  --features all \
  --max-features 10 \
  --memory-md true \
  --architecture-guard true \
  --security-review true \
  --constitution architecture_constitution.md \
  --mode review-ready \
  --stop-on-blockers true
```

## Next Recommended Commands

Use memory context before running the pipeline:

```text
/speckit.memory-md.plan-with-memory
```

Run the full pipeline:

```text
/speckit.reverse-spec.full-pipeline --source <repo> --target "<stack>"
```

After the pipeline completes, continue with:

```text
/speckit.memory-md.capture
/speckit.architecture-guard.architecture-review
/speckit.security-review.audit
/speckit.plan
/speckit.tasks
/speckit.implementation
/speckit.security-review.branch
/speckit.memory-md.capture-from-diff
```

### Notes

* `/speckit.architecture-guard.architecture-review` should run before `/speckit.plan`
* `/speckit.security-review.audit` should run before `/speckit.plan`
* `/speckit.security-review.branch` is only for reviewing implementation branch changes after code exists
* `/speckit.memory-md.capture-from-diff` should run after implementation changes exist
* Generated specs are **draft reconstructed artifacts**
* Human review is required before planning and implementation
* The pipeline orchestrates work but does not bypass architecture, security, or product decision gates
