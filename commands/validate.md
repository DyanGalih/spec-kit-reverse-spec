---
description: "Validate reverse-engineered feature folders for completeness, traceability, and review readiness."
---

# Command: /speckit.reverse-spec.validate

## Purpose
Check each generated feature folder for required files, required content, and unresolved questions before the artifacts move to architecture or security review.

## User Input
Use `$ARGUMENTS` to provide validation mode and blocker behavior.

Optional:
- `--mode <draft|review-ready|strict>`
- `--stop-on-blockers`

## Preconditions
- Feature folders exist under `specs/`.
- Generated files are readable.
- The validator can inspect `spec.md`, `source-traceability.md`, `architecture-alignment.md`, `security-considerations.md`, and `open-questions.md`.

## Procedure
1. Parse `$ARGUMENTS` conceptually and determine validation strictness and blocker handling.
2. Check every generated feature folder for the required file set.
3. Verify that `spec.md` contains functional requirements and acceptance criteria.
4. Verify that `source-traceability.md` ties feature behavior back to source files.
5. Verify that `architecture-alignment.md` exists and that `security-considerations.md` exists.
6. Categorize open questions as blocking or non-blocking.
7. Assign each feature one of the following statuses:
   - `READY_FOR_ARCHITECTURE_REVIEW`
   - `NEEDS_SOURCE_REVIEW`
   - `NEEDS_PRODUCT_DECISION`
   - `BLOCKED_BY_OPEN_QUESTIONS`
8. Write `.reverse-spec/validation-report.md`.

## Outputs
Produce:
- `.reverse-spec/validation-report.md`

## Failure Handling
- Stop on missing required files when `--stop-on-blockers` is enabled.
- Downgrade readiness when acceptance criteria or traceability are missing.
- Separate source gaps from product decisions so the review path stays clear.

## Quality Checklist
- Required files exist for each feature.
- `spec.md` includes functional requirements and acceptance criteria.
- `source-traceability.md` cites behavior evidence.
- `architecture-alignment.md` exists for every feature.
- `security-considerations.md` exists for every feature.
- Blocking and non-blocking questions are separated.

## Example Usage
```text
/speckit.reverse-spec.validate $ARGUMENTS --mode review-ready --stop-on-blockers
```

## Next Recommended Commands
- `/speckit.reverse-spec.export $ARGUMENTS`
- `/speckit.architecture-guard.architecture-review` if architecture issues remain
