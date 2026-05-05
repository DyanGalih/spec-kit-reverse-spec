# Reverse Spec Pipeline Report

## Source Repository
- [placeholder]

## Target Stack
- [placeholder]

## Pipeline Mode
- draft / review-ready / strict

## Optional Integrations Detected
- [ ] memory-md
- [ ] architecture-guard
- [ ] security-review

## Optional Integrations Missing
- [ ] memory-md
- [ ] architecture-guard
- [ ] security-review

## Features Detected
- [ ] [feature count or list placeholder]

## Specs Generated
- [ ] [count or path summary]

## Architecture Alignment Status
- [ ] complete
- [ ] partial
- [ ] blocked
- Notes: [placeholder]

## Security Preparation Status
- [ ] complete
- [ ] partial
- [ ] blocked
- Notes: [placeholder]

## Validation Status
- [ ] complete
- [ ] partial
- [ ] blocked
- Notes: [placeholder]

## Blocking Issues
- [ ] [blocking issue]

## Non-Blocking Issues
- [ ] [non-blocking issue]

## Recommended Next Commands
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

Notes:

- Run `/speckit.architecture-guard.architecture-review` before planning.
- Run `/speckit.security-review.audit` before planning.
- Run `/speckit.security-review.branch` only after implementation branch changes exist.
- Generated specs are draft reconstructed specs and require human review.

## Human Review Required
- [ ] Yes
- [ ] No
- Notes: [placeholder]

## Memory Capture Summary
- [ ] [summary of assumptions, findings, and decisions to carry forward]
