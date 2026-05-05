---
description: "Finalize reverse-engineered specs and generate export and pipeline reports."
---

# Command: /speckit.reverse-spec.export

## Purpose

Finalize the reconstructed specification folders with stable naming, mark them as draft reconstructed artifacts, and generate comprehensive export and pipeline reports. Produces delivery-ready reverse-spec outputs and prints the exact next-step commands for architecture review, security audit, and implementation planning.

Export is the handoff point: specs are complete, validated, and ready for team review and decision-making.

## User Input ($ARGUMENTS)

Use `$ARGUMENTS` to supply the source, target, and export scope.

**Required:**
- `--source <path-or-url>` — Source repository (for reference)
- `--target <stack>` — Target technology stack

**Optional:**
- `--features <list|all>` — Export specific features or all; default `all`
- `--output <dir>` — Output directory for reports; default `.reverse-spec`

## Preconditions

- Feature spec folders already exist under `specs/NNN-feature-name/`.
- Validation has been run or equivalent checks confirm spec completeness.
- All six template files (spec.md, reverse-analysis.md, architecture-alignment.md, security-considerations.md, open-questions.md, source-traceability.md) exist in each folder.
- The output directory is writable.

## Procedure

1. **Feature Folder Finalization**
   - Iterate over each selected feature folder under `specs/`.
   - For each spec.md, prepend a draft status block:
     ```
     > **⚠️ DRAFT: Reconstructed from Source**
     > 
     > This specification was reverse-engineered from source code, tests, and documentation.
     > It represents observed behavior, not requirements validated with product stakeholders.
     > Team review and refinement are required before implementation.
     > Generated: 2026-05-05 | Source: ./legacy-app | Target: NestJS + PostgreSQL
     ```
   - Confirm no changes to folder structure or core filenames.
   - Verify stable naming is preserved across exports (NNN never changes).

2. **Filename Stability Check**
   - Confirm each feature folder follows naming: `specs/NNN-feature-slug/`
   - Confirm filenames are exactly: spec.md, reverse-analysis.md, architecture-alignment.md, security-considerations.md, open-questions.md, source-traceability.md
   - Do not rename or reorganize; preserve traceability.

3. **Draft Status Verification**
   - Confirm every spec clearly identifies itself as a draft reconstructed artifact.
   - Check that no specification claims to be the final truth or prescriptive.
   - Ensure all open questions are visible and linked to blockers if applicable.

4. **Export Report Generation**
   - Create `.reverse-spec/export-report.md` with feature list, spec folder structure, status summary, and next steps.

5. **Pipeline Report Generation**
   - Create `.reverse-spec/pipeline-report.md` with exact copy-paste-ready commands for all downstream steps (architecture review, security audit, planning, implementation, security branch, context capture).

6. **Print Next Commands to Console**
   - Output the exact copy-paste-ready next commands to the terminal.

## Outputs

**Export Report** (`.reverse-spec/export-report.md`):
- List of exported features with status
- Feature folder locations and contents
- Summary of readiness across all features

**Pipeline Report** (`.reverse-spec/pipeline-report.md`):
- Complete workflow overview
- Quality gates and checkpoints
- Exact copy-paste commands for next steps (architecture, security, planning, implementation, etc.)
- Risks and reminders

**Console Output**:
- Next recommended commands printed to terminal

## Failure Handling

- **Missing `--source` or `--target`**: Stop immediately; both are required.
- **Feature folder missing**: Report which folder; suggest running extract first.
- **Missing template files**: Report which files; suggest running extract or validate first.
- **Export directory not writable**: Report permission error; suggest checking directory permissions.

## Quality Checklist

- [ ] `--source` and `--target` were provided explicitly.
- [ ] All selected feature folders exist and are complete.
- [ ] All specs are marked as "DRAFT: Reconstructed from Source".
- [ ] Stable numbering (NNN) is preserved.
- [ ] Filenames are consistent and stable.
- [ ] Export report is complete and links are valid.
- [ ] Pipeline report includes exact copy-paste commands.
- [ ] No specs claim to be final or prescriptive truth.
- [ ] All open questions are visible in feature folders.
- [ ] Next commands are printed to console.

## Example Usage

```text
/speckit.reverse-spec.export $ARGUMENTS \
  --source ./legacy-app \
  --target "NestJS + PostgreSQL" \
  --features all \
  --output .reverse-spec
```

## Next Recommended Commands

- `/speckit.memory-md.plan-with-memory` — Load memory context before architecture review
- `/speckit.architecture-guard.architecture-review` — Validate architecture assumptions
- `/speckit.security-review.audit` — Audit security implications
- `/speckit.plan` — Create implementation plan
- `/speckit.tasks` — Break down into tasks
- `/speckit.implementation` — Execute implementation
- `/speckit.security-review.branch` — Create security branch
- `/speckit.memory-md.capture-from-diff` — Capture context from changes
