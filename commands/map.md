---
description: "Map source architecture to target stack and architecture constitution."
---

# Command: /speckit.reverse-spec.map

## Purpose

Translate source components and layers into target-stack architecture placement. Identify drift, boundaries, and refactoring prerequisites before planning implementation. Ensures specifications understand architectural constraints and decisions before rebuilding begins.

Maps source reality to target aspirations without rewriting architecture blindly; surfaces mismatches that may require product or infrastructure decisions.

## User Input ($ARGUMENTS)

Use `$ARGUMENTS` to supply the target stack, constitution file, source repository, and optional feature scope.

**Required:**
- `--target <stack>` — Target technology stack (e.g., "Next.js + PostgreSQL")

**Optional:**
- `--constitution <path>` — Path to architecture constitution file; default `architecture_constitution.md`
- `--source <path-or-url>` — Source repository (for reference); same as extract/scan
- `--features <list|all>` — Comma-separated feature names, or `all`; default `all`

## Preconditions

- Target stack is known and specified via `--target`.
- `architecture_constitution.md` exists in the repository (or at path specified by `--constitution`), defining architectural rules and boundaries.
- Feature folders from `/speckit.reverse-spec.extract` exist under `specs/NNN-feature-name/`.
- Each feature folder contains `reverse-analysis.md` (source structure) and potentially `architecture-alignment.md` (to update).

## Procedure

1. **Load Constitution**
   - Read `architecture_constitution.md` (or `--constitution` path).
   - Extract architectural rules, constraints, and layer definitions:
     - **Layers**: Presentation, API, Business Logic, Persistence, Integration, etc.
     - **Boundaries**: Which layers can call which; request/response flows.
     - **Patterns**: Dependency injection, event-driven, synchronous vs. async, etc.
     - **Technology choices**: Framework constraints, database assumptions, cache patterns.
   - If constitution is missing, use generic target-stack defaults and warn user.

2. **Feature-by-Feature Architecture Alignment**
   - For each selected feature (or all if `--features all`):
     1. Read `reverse-analysis.md` to understand current source structure.
     2. Identify source components: which layers they touch, data flow, dependencies.
     3. Map to target stack:
        - Source controller → Target API handler / middleware
        - Source model → Target service / repository layer
        - Source background job → Target queue / worker process
        - Source middleware → Target guard / interceptor / middleware
     4. Document this mapping explicitly.

3. **Architecture Boundary Analysis**
   - For each feature, document the following boundaries and verify constitution compliance:
     - **Presentation Boundary**: UI <-> API contract (REST, GraphQL, etc.)
     - **Validation Boundary**: Where input validation occurs (presentation, API, service)
     - **Persistence Boundary**: Where data access happens (ORM, queries, repositories)
     - **API/Contract Boundary**: External services, third-party integrations
     - **Async/Background Boundary**: Job queues, event listeners, webhooks
     - **Integration Boundary**: How this feature interacts with other features
     - **Security/Trust Boundary**: Authentication, authorization, encryption, secrets management

4. **Drift and Refactor Analysis**
   - Identify cases where source architecture violates target constitution:
     - Source directly accesses database in controller → Should use repository layer
     - Source tightly couples features → Need service extraction
     - Source has synchronous third-party calls → Should be async via queue
   - For each drift, record:
     - **What**: The architectural violation (e.g., "Database access in controller")
     - **Why**: Why source does it (e.g., "Legacy monolith, no service layer")
     - **How to fix**: Refactoring needed before implementation (e.g., "Extract repository layer")
     - **Risk**: Impact if not fixed (e.g., "Tight coupling makes testing difficult")

5. **Architecture Alignment Documentation**
   - Generate or update `architecture-alignment.md` in each feature folder with complete mappings, boundaries, drift analysis, and refactor prerequisites.

6. **Constitution Compliance Check**
   - Verify each feature adheres to constitution rules.
   - Flag non-compliance items as refactor prerequisites.
   - Do not auto-fix; require explicit team decision.

## Outputs

**Updated Architecture Alignment Files** (per feature):
- `specs/NNN-feature-name/architecture-alignment.md` — Detailed mapping and drift analysis

**Architecture Report** (`.reverse-spec/architecture-report.md`):
- Summary of all features' architecture status
- Count of drift items per feature
- Prerequisites that block planning
- Constitution compliance summary

## Failure Handling

- **Missing `--target`**: Stop immediately; target stack is required.
- **Constitution file missing**: Use generic target-stack defaults and warn; require explicit constitution review before planning.
- **Feature folder missing**: Report which folder; suggest running extract first.
- **Ambiguous target stack**: Ask for clarification (e.g., "Next.js + MongoDB" vs. "Next.js + PostgreSQL" implies different security boundaries).
- **Unresolvable drift**: Mark as a blocker; require product or architecture team decision.

## Quality Checklist

- [ ] `--target` was provided explicitly.
- [ ] Architecture constitution is loaded and understood.
- [ ] Each feature has source-to-target mapping documented.
- [ ] All seven boundaries are explicitly addressed per feature.
- [ ] Drift items are clearly separated from design choices.
- [ ] Refactor prerequisites are actionable and linked to drift.
- [ ] No architectural decisions are assumed; all are explicit.
- [ ] Constitution compliance is verified and flagged if violated.

## Example Usage

```text
/speckit.reverse-spec.map $ARGUMENTS \
  --target "Next.js + PostgreSQL" \
  --constitution architecture_constitution.md \
  --source ./legacy-app \
  --features all
```

## Next Recommended Commands

- `/speckit.reverse-spec.validate $ARGUMENTS` — Validate completeness before architecture review.
- `/speckit.architecture-guard.architecture-review` — Deep architectural review using constitution.
- `/speckit.reverse-spec.export $ARGUMENTS` — Finalize specs after architecture alignment.
