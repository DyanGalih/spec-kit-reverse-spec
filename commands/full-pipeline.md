# Command: /speckit.reverse-spec.full-pipeline

Orchestrate the complete reverse-spec workflow WITHOUT breaking Spec Kit philosophy.

## Arguments
--source (required)
--target (required)
--output (default: .reverse-spec)
--features (default: all)
--max-features
--memory-md (default: true)
--architecture-guard (default: true)
--security-review (default: true)
--constitution (default: architecture_constitution.md)
--mode (draft | review-ready | strict)
--stop-on-blockers (default: true)

## Pipeline Logic

### A. PREFLIGHT
- Validate source repo and target stack.
- Detect `specs/` and `architecture_constitution.md`.
- Report installed extensions: `memory-md`, `architecture-guard`, `security-review`.

### B. MEMORY INTEGRATION
If `--memory-md true`:
- Before pipeline: Recommend `/speckit.memory-md.plan-with-memory`.
- After extraction: Recommend `/speckit.memory-md.capture`.
- After implementation: Recommend `/speckit.memory-md.capture-from-diff`.
- Optional: Recommend `/speckit.memory-md.audit`.

### C. SCAN
- Generate `.reverse-spec/` artifacts: `feature-inventory.md`, `source-map.md`, `assumptions.md`, `scan-report.md`.

### D. EXTRACT
- Generate `specs/NNN-feature/` with `spec.md`, `reverse-analysis.md`, `open-questions.md`, etc.
- **RULE:** Write behavior, NOT implementation.

### E. MAP
- Generate `architecture-alignment.md` in each feature spec.
- Alignment with target stack and `architecture_constitution.md`.

### F. SECURITY PREP
- Generate `security-considerations.md`.
- **DO NOT RUN:** `speckit.security-review.branch`.
- **ONLY recommend:** `/speckit.security-review.audit`.

### G. VALIDATE
- Generate `.reverse-spec/validation-report.md`.
- Check status: `READY_FOR_ARCHITECTURE_REVIEW`, etc.

### H. EXPORT
- Generate `.reverse-spec/export-report.md` and `.reverse-spec/pipeline-report.md`.

## 🚦 QUALITY GATES

Print EXACT next commands:

```text
/speckit.memory-md.plan-with-memory
/speckit.reverse-spec.full-pipeline --source <repo> --target "<stack>"
/speckit.memory-md.capture
/speckit.architecture-guard.architecture-review
/speckit.security-review.audit
/speckit.plan
/speckit.tasks
/speckit.implementation
/speckit.security-review.branch
/speckit.memory-md.capture-from-diff
```
