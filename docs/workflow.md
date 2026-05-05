# Workflow

Reverse Spec Kit follows a draft-first workflow that turns source behavior into Spec Kit-ready artifacts without claiming final truth.

## 1. Scan

Use `/speckit.reverse-spec.scan` to inventory likely features, entry points, and source evidence. This step separates product behavior from infrastructure helpers and records confidence for each feature.

## 2. Extract

Use `/speckit.reverse-spec.extract` to create draft feature folders under `specs/`. Each folder should describe the rebuilt system's behavior, acceptance criteria, assumptions, and open questions.

## 3. Map

Use `/speckit.reverse-spec.map` to align each feature against the target stack and architecture constitution. This step records drift and the refactors required before planning.

## 4. Validate

Use `/speckit.reverse-spec.validate` to check required files, traceability, and readiness status. Validation should make blockers obvious instead of hiding them.

## 5. Export

Use `/speckit.reverse-spec.export` to stabilize filenames, finalize the draft set, and write export and pipeline reports.

## 6. Review and Continue

After export, continue with memory, architecture, and security review commands before planning and implementation.

```text
/speckit.memory-md.plan-with-memory
/speckit.memory-md.capture
/speckit.architecture-guard.architecture-review
/speckit.security-review.audit
/speckit.plan
/speckit.tasks
/speckit.implementation
/speckit.security-review.branch
/speckit.memory-md.capture-from-diff
```

`/speckit.security-review.branch` is only for reviewing implementation branch changes after code exists.

## Important Rule

Reverse Spec Kit documents the rebuilt system's expected behavior. It does not bless the source architecture as the target architecture.
