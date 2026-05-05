---
description: "Map source architecture to the target stack and architecture constitution."
---

# Command: /speckit.reverse-spec.map

## Purpose
Translate source components into target-stack architectural placement and record the drift, boundaries, and refactors needed before planning.

## User Input
Use `$ARGUMENTS` to supply the target stack, constitution file, source repository, and optional feature scope.

Required:
- `--target <stack>`

Optional:
- `--constitution <path>`
- `--source <path-or-url>`
- `--features <list|all>`

## Preconditions
- A target stack is known or auto-detectable from the project.
- `architecture_constitution.md` or the supplied constitution file is available when architectural rules must be checked.
- Feature folders from extraction exist or can be referenced.

## Procedure
1. Parse `$ARGUMENTS` conceptually and resolve the target stack, constitution path, source context, and feature filter.
2. Read `architecture_constitution.md` when available and use it as the governing architectural reference.
3. For each feature, compare source components against the target stack.
4. Produce `architecture-alignment.md` per feature with:
   - target stack
   - source components
   - target components
   - layer mapping
   - business logic placement
   - validation boundary
   - persistence boundary
   - API/contract boundary
   - async/background boundary
   - integration boundary
   - security/trust boundary
   - Architecture Guard checklist
   - known drift from source
   - required refactor before planning
5. Record mismatches, source coupling, and placement risks without auto-correcting architecture decisions.

## Outputs
Produce or refresh `architecture-alignment.md` for each extracted feature folder.

## Failure Handling
- Stop when no target stack is provided and no safe auto-detection exists.
- Flag missing constitution data as a review gap.
- Surface source drift instead of hiding it behind target assumptions.

## Quality Checklist
- Target stack and source context are both visible.
- Boundaries are explicitly separated.
- Drift is documented.
- Refactor prerequisites are clear before planning starts.

## Example Usage
```text
/speckit.reverse-spec.map $ARGUMENTS --target "Next.js + PostgreSQL" --constitution architecture_constitution.md --source ./legacy-app --features all
```

## Next Recommended Commands
- `/speckit.reverse-spec.validate $ARGUMENTS`
- `/speckit.architecture-guard.architecture-review` when the architecture guard integration is enabled
