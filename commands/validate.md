# Command: /speckit.reverse-spec.validate

Validate the reverse-engineered specs for completeness and alignment.

## Arguments
--mode (draft | review-ready | strict): Validation strictness.
--stop-on-blockers (default: true): Halt if critical issues are found.

## Behavior
1. Check all `specs/` for required documentation.
2. Verify alignment with `architecture_constitution.md`.
3. Generate `.reverse-spec/validation-report.md`.
4. Assign statuses:
   - READY_FOR_ARCHITECTURE_REVIEW
   - BLOCKED_BY_OPEN_QUESTIONS
   - NEEDS_PRODUCT_DECISION
