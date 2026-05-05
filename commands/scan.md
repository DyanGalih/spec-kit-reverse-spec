---
description: "Scan a source repository, classify product features, and generate the reverse-spec inventory with confidence labels."
---

# Command: /speckit.reverse-spec.scan

## Purpose

Inspect a source codebase end-to-end and produce a structured feature inventory, source map, assumptions log, and scan report that downstream commands refine into specifications. Separates product features from infrastructure, assigns confidence levels based on evidence consistency, and records all assumptions explicitly.

The scan establishes the factual foundation—what routes exist, what tests cover, what docs describe—without rewriting implementation details as requirements.

## User Input ($ARGUMENTS)

Use `$ARGUMENTS` to supply the source repository and optional scope filters.

**Required:**
- `--source <path-or-url>` — Relative or absolute path, or git clone URL of the repository to scan

**Optional:**
- `--target <stack>` — Target technology stack (e.g., "NestJS + PostgreSQL", "React + Next.js")
- `--output <dir>` — Output directory for scan artifacts; default `.reverse-spec`
- `--depth <n>` — Traversal depth (0-5); higher = more thorough; default `3`
- `--include-tests` — Include test suites in signal collection; default `true`
- `--include-docs` — Include documentation and examples in signal collection; default `true`
- `--exclude <pattern>` — Glob pattern to exclude files (e.g., `vendor/**,node_modules/**`); can be repeated

## Preconditions

- The source repository exists and is readable (local path or cloneable URL).
- `--source` must be provided explicitly.
- The output directory is writable (will be created if missing).
- The system has permission to read all repository files, or exclusion rules are set to skip restricted paths.

## Procedure

1. **Repository Access**
   - Clone or mount the source repository at `--source`.
   - If the URL cannot be cloned, treat it as a local path; fail clearly if neither works.
   - Confirm all exclusion patterns compile without syntax errors.

2. **Signal Collection**
   - Traverse the repository to depth `--depth` and collect signals from:
     - Routes / URL mappings (Express, NestJS, Rails, Next.js, etc.)
     - Controllers / request handlers
     - Pages and UI components (React, Vue, Svelte, etc.)
     - Data models (ActiveRecord, Prisma, TypeORM, etc.)
     - Database migrations
     - API endpoint definitions and schemas
     - CLI commands and subcommands
     - Background jobs / async workers / event listeners
     - Service classes and business logic modules
     - Test suites (unit, integration, e2e)
     - Documentation files, examples, and inline comments
   - Apply `--exclude` patterns to skip vendor, build, cache, and credential files.
   - If `--include-tests false`, skip test files but do record test count and coverage hints.
   - If `--include-docs false`, skip documentation but do count docs present.

3. **Feature Extraction**
   - Group signals into candidate features by functional coherence (e.g., "User Authentication", "Payment Processing", "Email Notifications").
   - Separate product features from infrastructure:
     - **Product features**: Directly implement user stories (auth, billing, reporting, etc.).
     - **Infrastructure**: Build tools, deployment config, logging, monitoring, dependency management, health checks.
   - Record entry points: the route, handler, or CLI command that initiates the feature.

4. **Confidence Assignment**
   - `HIGH`: Routes + tests + docs/comments all describe the same behavior consistently.
   - `MEDIUM`: Routes + source code agree; tests or docs are missing but don't contradict source.
   - `LOW`: Feature inferred from source structure only (e.g., a service with no test or route evidence).
   - Include confidence *reason* (e.g., "HIGH: auth routes, password tests, and README security section agree on session lifetime").

5. **Assumption Logging**
   - Record all assumptions made during signal collection (e.g., "Assumed `POST /users` creates a user account because route name and test names suggest it").
   - Note gaps: "No test for edge case X" or "Docs mention feature Y but no code found".
   - Do not rewrite assumptions as facts; preserve ambiguity for downstream review.

6. **Artifact Writing**
   - Write all scan outputs to the `--output` directory (default `.reverse-spec`).
   - Create or overwrite:
     - `.reverse-spec/feature-inventory.md`
     - `.reverse-spec/source-map.md`
     - `.reverse-spec/assumptions.md`
     - `.reverse-spec/scan-report.md`

## Outputs

**Feature Inventory** (`.reverse-spec/feature-inventory.md`):
- List of discovered product features with entry points, signal sources, and confidence labels.
- Format:
  ```
  ### Feature: User Authentication
  - Confidence: HIGH
  - Reason: Routes (auth/login, auth/logout), tests (spec/auth.spec.js), README
  - Entry Points: POST /auth/login, POST /auth/logout
  - Source Files: app/controllers/auth.js, app/models/user.js
  - Tests: spec/auth.spec.js (42 tests)
  - Docs: README security section
  ```

**Source Map** (`.reverse-spec/source-map.md`):
- Directory and file structure with annotations for product vs. infrastructure layers.
- Count files by type: routes, controllers, models, tests, docs.
- Example:
  ```
  src/
    app/
      controllers/        [product: 12 files]
      models/            [product: 8 files]
      middleware/        [infrastructure: 4 files]
    tests/
      unit/              [product: 15 files]
      integration/       [product: 3 files]
  ```

**Assumptions Log** (`.reverse-spec/assumptions.md`):
- Explicit list of inferences, heuristics, and gaps.
- Example:
  ```
  - Assumed `User.sendWelcomeEmail()` is called on signup because method exists and test name is `sendWelcomeEmail`.
  - Could not find tests for password reset flow; inferred from routes only.
  - No docs for multi-tenant separation; checking code for evidence.
  ```

**Scan Report** (`.reverse-spec/scan-report.md`):
- Summary: repository size, language, framework, artifact count, confidence distribution.
- Warnings: excluded paths, unreadable files, patterns with LOW confidence.
- Recommendations: features recommended for extraction, features deferred due to confidence or complexity.

## Failure Handling

- **Missing `--source`**: Stop immediately with error message requiring `--source`.
- **Unreadable repository**: Report which paths failed, suggest checking permissions or using `--exclude`.
- **Exclusion removes all files**: Warn that the `--exclude` pattern is too broad; confirm intent.
- **Sparse evidence**: Assign LOW confidence and record assumption instead of guessing.
- **Conflicting signals** (e.g., route name says "delete" but tests say "archive"): Record both; do not assume one is wrong.

## Quality Checklist

- [ ] Source repository was resolved (local or cloned) without errors.
- [ ] `--source` was provided explicitly; no auto-defaults were used.
- [ ] Candidate features are clearly separated from infrastructure.
- [ ] Every feature has a confidence label with a documented reason.
- [ ] Assumptions are recorded separately from evidence.
- [ ] Exclusion patterns did not accidentally hide important files.
- [ ] All four scan artifacts exist and are readable YAML/Markdown.
- [ ] Scan report includes a summary of confidence distribution (count of HIGH, MEDIUM, LOW).

## Example Usage

```text
/speckit.reverse-spec.scan $ARGUMENTS \
  --source ./legacy-app \
  --target "NestJS + PostgreSQL" \
  --output .reverse-spec \
  --depth 4 \
  --include-tests \
  --include-docs \
  --exclude "node_modules/**,dist/**,.env*,*.test.js"
```

## Next Recommended Commands

- `/speckit.reverse-spec.extract $ARGUMENTS` — Extract draft specs from scanned features.
- `/speckit.memory-md.plan-with-memory $ARGUMENTS` — If memory-md is installed, review scan results in context before extraction.
- `/speckit.reverse-spec.full-pipeline $ARGUMENTS` — Run the entire reverse-spec workflow from scratch instead of continuing step-by-step.
