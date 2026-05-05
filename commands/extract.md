---
description: "Extract draft reconstructed feature specifications from source behavior and scan inventory."
---

# Command: /speckit.reverse-spec.extract

## Purpose

Convert discovered source behavior into draft Spec Kit-compatible feature specification folders. Each folder describes **what the rebuilt system must do**, not how the original code implements it.

Extract transforms evidence (routes, tests, docs, source code) into specifications that teams can review, refactor, and build forward from. It preserves traceability to source while avoiding implementation bias.

## User Input ($ARGUMENTS)

Use `$ARGUMENTS` to provide the source, target stack, feature scope, and optional integration toggles.

**Required:**
- `--source <path-or-url>` — Source repository (same as scan)
- `--target <stack>` — Target technology stack (e.g., "React + Node.js")

**Optional:**
- `--features <list|all>` — Comma-separated feature names, or `all`; default `all`
- `--max-features <n>` — Cap the number of features to extract (0 = unlimited); default `0`
- `--architecture-guard` — Enable architecture alignment cross-checks; default `true`
- `--security-review` — Enable security considerations output; default `true`
- `--memory-md` — Reference memory context if available; default `true`

## Preconditions

- `--source` and `--target` are both provided.
- `.reverse-spec/feature-inventory.md` is available (from a prior scan) OR the command will run scan inline.
- The `specs/` output path is writable (will be created if missing).
- Target stack is known and valid (e.g., "Next.js + PostgreSQL" or "Express + MongoDB").

## Procedure

1. **Resolve Scan Results**
   - Check if `.reverse-spec/feature-inventory.md` exists and is readable.
   - If yes, load and reuse the scan results.
   - If no, run scan behavior inline using `--source` and available scope options to generate the inventory.
   - Confirm all required scan artifacts exist before proceeding.

2. **Feature Selection**
   - Parse `--features` and determine which discovered features to extract.
   - If `--features all`, extract all product features from the inventory.
   - If `--features auth,billing`, extract only those named features (must match feature names in inventory).
   - If `--max-features 5`, stop after the 5th feature and log which features were deferred.
   - Default confidence-based ordering: HIGH confidence features first, then MEDIUM, then LOW.

3. **Spec Folder Creation**
   - For each selected feature, create a stable numbered folder: `specs/NNN-feature-slug/`
     - NNN = 001, 002, 003, ... (zero-padded, assigned in stable order)
     - feature-slug = lowercase, hyphens-only version of feature name
     - Example: `specs/001-user-authentication/`, `specs/002-payment-processing/`
   - Do not renumber folders on subsequent runs; preserve stable numbering.

4. **Template Generation**
   - For each feature folder, generate the required template files (project templates should be in `templates/`):
     - `spec.md` — Core feature specification (from `spec.template.md`)
     - `reverse-analysis.md` — How the source implements the feature (from `reverse-analysis.template.md`)
     - `architecture-alignment.md` — How the feature maps to target architecture (from `architecture-alignment.template.md`)
     - `security-considerations.md` — Security implications (from `security-considerations.template.md`)
     - `open-questions.md` — Ambiguities and decisions needed (from `open-questions.template.md`)
     - `source-traceability.md` — Links to source evidence (from `source-traceability.template.md`)

5. **Content Population**
   - **spec.md**: Extract functional requirements from routes, tests, and docs. Write in imperative voice: "The system must allow users to reset their password by email link." Do not write "The code calls `sendResetEmail()`".
   - **reverse-analysis.md**: Describe how the current source implements the behavior. Example: "Routes POST /auth/reset; model User has sendResetEmail() method; tests confirm token expiry."
   - **architecture-alignment.md**: Describe target architecture placement. Example: "Auth service in API tier; token validation in middleware; email via Queue/Worker."
   - **security-considerations.md**: List security implications. Example: "Tokens must be short-lived; reset links single-use; rate-limit reset requests."
   - **open-questions.md**: Record ambiguities. Example: "Should reset tokens expire? Should reset link be single-use? Should email domain be verified?"
   - **source-traceability.md**: Map behavior to source files. Example: "POST /auth/reset → routes/auth.js:45; test → spec/auth.spec.js:123; implementation → models/user.js:234."

6. **Integration Cross-Checks**
   - If `--architecture-guard true`, check that architecture assumptions are explicit (e.g., which tier handles validation?).
   - If `--security-review true`, confirm that security-considerations.md flags all identified risks.
   - If `--memory-md true`, note memory context (if available from prior `/speckit.memory-md.capture`).

7. **Artifact Finalization**
   - Confirm all spec folders are complete and valid.
   - Write or refresh `.reverse-spec/extraction-report.md` (lists extracted features, confidence distribution, deferred features).

## Outputs

**Feature Spec Folders** (under `specs/`):
- `specs/001-feature-name/spec.md`
- `specs/001-feature-name/reverse-analysis.md`
- `specs/001-feature-name/architecture-alignment.md`
- `specs/001-feature-name/security-considerations.md`
- `specs/001-feature-name/open-questions.md`
- `specs/001-feature-name/source-traceability.md`
- (Repeat for all selected features)

**Extraction Report** (`.reverse-spec/extraction-report.md`):
- List of extracted features with confidence levels.
- Count of open questions per feature (total blocking, non-blocking).
- Deferred features and reason.

## Failure Handling

- **Missing `--source` or `--target`**: Stop immediately; both are required.
- **No scan results and scan fails**: Report which scan step failed; suggest running scan manually first.
- **Feature not found in inventory**: Report available feature names; suggest checking feature name spelling.
- **Spec folder already exists**: Overwrite with new content and preserve stable numbering; report the conflict if the folder is not writable.
- **Template file missing**: Use a fallback minimal template and warn user.
- **Uncertain behavior**: Mark as an open question instead of inventing a requirement.

## Quality Checklist

- [ ] `--source` and `--target` were both provided.
- [ ] Scan results were loaded or generated inline without errors.
- [ ] Each selected feature has a numbered spec folder with stable naming.
- [ ] All six template files exist in each folder.
- [ ] `spec.md` describes required behavior in imperative voice, not implementation mechanics.
- [ ] `reverse-analysis.md` ties behavior back to source evidence with file paths and line numbers.
- [ ] `architecture-alignment.md` identifies target placement (layers, boundaries, risks).
- [ ] `security-considerations.md` lists all identified security implications.
- [ ] `open-questions.md` captures ambiguities; questions are marked blocking or non-blocking.
- [ ] `source-traceability.md` provides clickable links or file:line references to source.
- [ ] Extraction report shows confidence distribution and deferred features.

## Example Usage

```text
/speckit.reverse-spec.extract $ARGUMENTS \
  --source ./legacy-app \
  --target "React + Node.js" \
  --features auth,billing,reporting \
  --max-features 10 \
  --architecture-guard \
  --security-review \
  --memory-md
```

## Next Recommended Commands

- `/speckit.reverse-spec.map $ARGUMENTS` — Map extracted features to target architecture.
- `/speckit.reverse-spec.validate $ARGUMENTS` — Validate completeness before review.
- `/speckit.architecture-guard.architecture-review` — Cross-check architecture assumptions.
