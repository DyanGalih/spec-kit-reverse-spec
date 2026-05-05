# Validation Report

## Summary
- Validation mode: [draft / review-ready / strict]
- Overall status: [placeholder]
- Total features checked: [placeholder]

## Feature Status Table
| Feature | Status | Missing Files | Traceability | Architecture | Security | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [feature] | READY_FOR_ARCHITECTURE_REVIEW / NEEDS_SOURCE_REVIEW / NEEDS_PRODUCT_DECISION / BLOCKED_BY_OPEN_QUESTIONS | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] |
| [feature] | READY_FOR_ARCHITECTURE_REVIEW / NEEDS_SOURCE_REVIEW / NEEDS_PRODUCT_DECISION / BLOCKED_BY_OPEN_QUESTIONS | [placeholder] | [placeholder] | [placeholder] | [placeholder] | [placeholder] |

## Blocking Issues
- [ ] [issue blocking progress]
- [ ] [issue blocking progress]

## Non-Blocking Issues
- [ ] [issue to fix later]
- [ ] [issue to fix later]

## Missing Files
- [ ] `spec.md`
- [ ] `reverse-analysis.md`
- [ ] `architecture-alignment.md`
- [ ] `security-considerations.md`
- [ ] `open-questions.md`
- [ ] `source-traceability.md`

## Architecture Readiness
- [ ] Ready
- [ ] Needs review
- [ ] Drift documented
- Notes: [placeholder]

## Security Readiness
- [ ] Ready
- [ ] Needs review
- [ ] Sensitive behavior captured
- Notes: [placeholder]

## Recommended Next Commands
```text
/speckit.reverse-spec.export
/speckit.architecture-guard.architecture-review
/speckit.security-review.audit
```

Notes:

- Export generates final handoff reports.
- Architecture review should happen before `/speckit.plan`.
- Security audit should happen before `/speckit.plan`.
- Do not run `/speckit.security-review.branch` until implementation branch changes exist.
