# Quality Gates

Reverse Spec Kit uses explicit readiness states so teams can see whether the generated draft specs are ready for architecture review, still missing source evidence, or blocked by product decisions.

## Validation Statuses

- `READY_FOR_ARCHITECTURE_REVIEW`
- `NEEDS_SOURCE_REVIEW`
- `NEEDS_PRODUCT_DECISION`
- `BLOCKED_BY_OPEN_QUESTIONS`

## What Each Gate Means

### READY_FOR_ARCHITECTURE_REVIEW

The feature folder has the required files, functional requirements, acceptance criteria, traceability, architecture alignment, and security considerations.

### NEEDS_SOURCE_REVIEW

The spec exists, but source evidence is incomplete or weak. Re-check routes, tests, docs, or entry points before planning.

### NEEDS_PRODUCT_DECISION

The extracted behavior is understandable, but the product direction is not resolved well enough to treat it as ready.

### BLOCKED_BY_OPEN_QUESTIONS

The feature cannot move forward until blocking questions are answered.

## Recommended Command Flow

```text
/speckit.memory-md.plan-with-memory
/speckit.reverse-spec.scan
/speckit.reverse-spec.extract
/speckit.reverse-spec.map
/speckit.reverse-spec.validate
/speckit.reverse-spec.export
```

Then continue with:

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

## Post-Implementation Gates

After implementation changes exist:

1. Run `/speckit.security-review.branch` to review branch changes.
2. Run `/speckit.memory-md.capture-from-diff` to capture durable decisions and implementation learnings.
3. Do not run branch review before implementation code exists.
