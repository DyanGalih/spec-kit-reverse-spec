# Integration Guide

Reverse Spec Kit is built to cooperate with memory, architecture, and security extensions instead of replacing them.

## Memory-MD

Use memory-md when you want durable context across a migration or reverse-engineering effort.

- Before pipeline work: `/speckit.memory-md.plan-with-memory`
- During or after reverse-spec work: run `/speckit.memory-md.capture` to record assumptions, source findings, mappings, and decisions.
- After source changes exist: `/speckit.memory-md.capture-from-diff`

## Architecture-Guard

Use architecture-guard when you need the generated specs compared against a real target architecture policy.

- It is most useful after map and validate.
- It should review drift instead of trying to erase it.

## Security-Review

Use security-review to examine threat surface, authorization, data exposure, and migration risk.

- Run `/speckit.security-review.audit` before planning.
- Run `/speckit.security-review.branch` only after implementation branch changes exist.

## Suggested Sequence

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

## Notes

- Missing integrations should not block the reverse-spec pipeline by themselves.
- Review commands are recommendations, not hidden auto-runs.
