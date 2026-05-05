---
description: "Validate reverse-engineered feature folders for completeness, traceability, and review readiness."
---

# Command: /speckit.reverse-spec.validate

## Purpose

Inspect all generated feature folders for required files, required content depth, and unresolved questions. Classify each feature's readiness for architecture review, security audit, or product refinement. Ensures specifications are complete enough for team review before moving to implementation planning.

## User Input ($ARGUMENTS)

Use `$ARGUMENTS` to provide validation mode and blocker behavior.

**Optional:**
- `--mode <draft|review-ready|strict>` — Validation strictness level; default `review-ready`
- `--stop-on-blockers <true|false>` — Exit with error if blocking issues found; default `true`
- `--features <list|all>` — Validate specific features or all; default `all`

## Preconditions

- Feature folders exist under `specs/NNN-feature-name/`.
- Generated files (`spec.md`, `reverse-analysis.md`, `architecture-alignment.md`, `security-considerations.md`, `open-questions.md`, `source-traceability.md`) are readable.
- Prior extract, map, and optional security review have been completed.

## Procedure

1. **Validation Mode Setup**
   - **draft**: Minimal validation; file presence only; quiet on content gaps.
   - **review-ready**: Standard validation; content depth required; warnings on gaps.
   - **strict**: Maximal validation; all content must be detailed; block on any gap.
   - Set warning threshold and exit behavior accordingly.

2. **Iterate Over All Features**
   - For each feature folder under `specs/`, run the following checks:

3. **File Presence Check**
   - Verify all six files exist:
     - [ ] `spec.md`
     - [ ] `reverse-analysis.md`
     - [ ] `architecture-alignment.md`
     - [ ] `security-considerations.md`
     - [ ] `open-questions.md`
     - [ ] `source-traceability.md`
   - If mode=`draft`: warn if missing; continue.
   - If mode=`review-ready`: fail if any file missing; stop feature validation.
   - If mode=`strict`: fail if any file missing; stop feature validation.

4. **spec.md Content Validation**
   - Check that `spec.md` contains:
     - [ ] Feature name / title
     - [ ] Purpose or goal statement
     - [ ] **Functional requirements** (at least 3; written in "the system must..." language)
     - [ ] **Acceptance criteria** (at least 2 per requirement; GIVEN/WHEN/THEN or equivalent)
     - [ ] Scope (what's in / out)
   - Validate that requirements are **behavior-focused**, not implementation-focused:
     - ✅ "System must accept user login via email and password."
     - ❌ "System will call `authenticate(email, password)` method."
   - Record finding: PASS, WARN (content thin), or FAIL (missing sections).

5. **source-traceability.md Validation**
   - Check that `source-traceability.md` contains:
     - [ ] List of source files with line numbers or file:line references
     - [ ] Tests that exercise the feature (count and names)
     - [ ] Documentation references (if any exist in source)
     - [ ] Mapping of feature behavior to source locations
   - Verify at least one source file is cited per requirement.
   - Verify traceability is specific (file:line, not just "src/controllers/").
   - Record finding: PASS, WARN (sparse), or FAIL (missing).

6. **architecture-alignment.md Validation**
   - Check that `architecture-alignment.md` contains:
     - [ ] Target stack identification
     - [ ] Source-to-target layer mapping (source components → target placement)
     - [ ] All seven boundaries documented: Presentation, Validation, Persistence, API/Contract, Async, Integration, Security
     - [ ] Known drift from source to target (if any)
     - [ ] Refactor prerequisites (if any)
   - Record finding: PASS, WARN (boundary gaps), or FAIL (missing sections).

7. **security-considerations.md Validation**
   - Check that `security-considerations.md` contains:
     - [ ] Security implications identified (at least 2)
     - [ ] Data sensitivity classifications (public, confidential, secret, etc.)
     - [ ] Authentication/authorization requirements
     - [ ] Encryption or data protection measures
     - [ ] Third-party dependencies and trust assumptions
     - [ ] Known risks or mitigations
   - Record finding: PASS, WARN (gaps), or FAIL (missing).

8. **open-questions.md Classification**
   - Read `open-questions.md` and classify each question as:
     - **BLOCKING**: Must be resolved before implementation can start (e.g., "Should tokens be refreshed automatically?")
     - **NON-BLOCKING**: Can be resolved during implementation or refinement (e.g., "Should we log all login attempts?")
   - Count blocking and non-blocking questions.
   - If `mode=strict` and any blocking question exists, mark feature as BLOCKED.

9. **Readiness Classification**
   - Assign each feature one of four statuses:
     - **READY_FOR_ARCHITECTURE_REVIEW**: All files complete, no critical gaps, architecture assumptions explicit, no blocking questions.
     - **NEEDS_SOURCE_REVIEW**: Traceability sparse or unclear; source code review required before architecture review.
     - **NEEDS_PRODUCT_DECISION**: Open blocking questions; product team input needed.
     - **BLOCKED_BY_OPEN_QUESTIONS**: Blocking questions prevent any further work.

10. **Validation Report Generation**
    - Generate `.reverse-spec/validation-report.md` with complete findings per feature, status summary, and recommendations.

## Outputs

**Validation Report** (`.reverse-spec/validation-report.md`):
- Complete validation results per feature
- Status classification per feature
- Blocking issues summary
- Next steps recommendations

## Failure Handling

- **No feature folders found**: Report which directory was searched; suggest running extract first.
- **Missing required file**: If `--mode review-ready` or `strict`, mark feature as incomplete and continue or stop based on `--stop-on-blockers`.
- **Content too sparse**: Warn in report; downgrade readiness status; do not auto-fail.
- **Ambiguous requirements**: Suggest clarification but do not block; mark as open question.
- **Too many blocking questions**: Flag feature as BLOCKED_BY_OPEN_QUESTIONS; require product decision before proceeding.

## Quality Checklist

- [ ] `--mode` was set to appropriate level (draft, review-ready, or strict).
- [ ] All feature folders were validated according to mode.
- [ ] spec.md includes functional requirements and acceptance criteria.
- [ ] source-traceability.md cites source files with file:line specificity.
- [ ] architecture-alignment.md documents all required boundaries.
- [ ] security-considerations.md lists identified security implications.
- [ ] Open questions are classified as blocking or non-blocking.
- [ ] Each feature is assigned a readiness status.
- [ ] Validation report is complete and actionable.
- [ ] Blocking issues are visible and prioritized.

## Example Usage

```text
/speckit.reverse-spec.validate $ARGUMENTS \
  --mode review-ready \
  --stop-on-blockers true \
  --features all
```

## Next Recommended Commands

- `/speckit.reverse-spec.export $ARGUMENTS` — Finalize and export specs for delivery.
- `/speckit.architecture-guard.architecture-review` — Review architecture assumptions.
- `/speckit.security-review.audit` — Deep security audit of specifications.
- Product team review if NEEDS_PRODUCT_DECISION status appears.
