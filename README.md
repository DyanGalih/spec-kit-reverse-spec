# 🔄 Reverse Spec Kit

Reverse Spec reverse-engineers OSS repositories into Spec Kit-compatible feature specs for rebuilding in a target stack.

![Version](https://img.shields.io/badge/version-0.1.1-22c55e)
![Spec Kit](https://img.shields.io/badge/Spec%20Kit-compatible-2563eb)
![Reverse Engineering](https://img.shields.io/badge/role-reverse--engineering-blue)
![License](https://img.shields.io/badge/license-MIT-f59e0b)

## Overview

Reverse Spec Kit adds a governed reverse-engineering flow to Spec Kit projects. It scans an existing OSS repository, detects product features, extracts draft reconstructed specs from source behavior, maps the source architecture to a target architecture, prepares security considerations, and validates and exports the generated artifacts.

It is intended for migration and modernization work where the source repository is evidence, but the rebuilt system should still be planned with Spec Kit conventions, review gates, and architecture governance.

## What This Extension Does

- Scans source OSS repositories.
- Detects candidate product features.
- Extracts observed behavior into draft reconstructed specs.
- Maps source architecture to the target architecture.
- Prepares security considerations for review.
- Validates and exports the generated specs.

## What This Extension Does Not Do

- It does not generate implementation.
- It does not auto-run `/speckit.implementation`.
- It does not auto-fix architecture.
- It does not replace human or product validation.
- It does not blindly preserve source architecture.
- It does not treat generated specs as final truth.

## How It Fits Spec Kit

Reverse Spec is a companion extension for reverse-engineering existing repositories into Spec Kit-ready feature artifacts.

It works alongside:

- `memory-md` for durable assumptions, decisions, and source findings.
- `architecture-guard` for target-architecture alignment and governed delivery.
- `security-review` for security analysis before planning and implementation.

The reverse-spec flow is draft-first: it produces reconstructed specs and review artifacts, then hands off to architecture, security, planning, and implementation workflows.

## Installation

### Install from Local Development Checkout

```bash
specify extension add --dev /path/to/spec-kit-reverse-spec
```

### Install from GitHub Release

```bash
specify extension add reverse-spec --from https://github.com/DyanGalih/spec-kit-reverse-spec/archive/refs/tags/v0.1.1.zip
```

### Install from Catalog After Publication

```bash
specify extension add reverse-spec
```

Only use the catalog install form after the extension is available in the configured catalog.

## Command Split

- `/speckit.reverse-spec.scan` scans the source repository and builds the feature inventory.
- `/speckit.reverse-spec.extract` generates draft reconstructed feature specs.
- `/speckit.reverse-spec.map` maps source components to the target architecture and constitution.
- `/speckit.reverse-spec.validate` checks feature folders for completeness and readiness.
- `/speckit.reverse-spec.export` finalizes the draft set and writes export reports.
- `/speckit.reverse-spec.full-pipeline` orchestrates scan, extract, map, validate, and export without skipping review gates.

## Usage

Use `$ARGUMENTS` with the registered slash commands to control scope, target stack, and pipeline behavior.

### Full Pipeline

```bash
/speckit.reverse-spec.full-pipeline --source ../oss-repo --target "Laravel + Inertia + Vue"
```

The full pipeline is orchestrated, not autopiloted. It keeps the generated specs as drafts and recommends follow-up governance commands instead of auto-running implementation.

### Scoped Extraction

```bash
/speckit.reverse-spec.extract --source ../oss-repo --target "NestJS + React + PostgreSQL" --features auth,billing --max-features 5
```

### Architecture Mapping

```bash
/speckit.reverse-spec.map --source ../oss-repo --target "Laravel + Inertia + Vue" --constitution architecture_constitution.md
```

## Workflow Integration

### Memory-MD Integration

Use only:

- `/speckit.memory-md.plan-with-memory`
- `/speckit.memory-md.capture`
- `/speckit.memory-md.capture-from-diff`
- `/speckit.memory-md.audit`
- `/speckit.memory-md.log-finding`

Recommended use:

- Plan with memory before the reverse-spec pipeline.
- Capture memory after reverse-spec artifacts are generated.
- Capture from diff after implementation changes exist.
- Audit memory when the project context needs a review.
- Log findings when you discover important source behavior, assumptions, or migration context.

### Architecture Guard Integration

Use:

- `/speckit.architecture-guard.architecture-review`

Optional if installed:

- `/speckit.architecture-guard.governed-plan`
- `/speckit.architecture-guard.governed-tasks`
- `/speckit.architecture-guard.governed-implement`

Architecture Guard helps compare reconstructed specs against the target architecture and constitution instead of copying the source structure blindly.

### Security Review Integration

Use:

- `/speckit.security-review.audit` before planning
- `/speckit.security-review.branch` after implementation changes

If the audit produces findings, you can also use:

- `/speckit.security-review.followup`
- `/speckit.security-review.apply`

Security Review evaluates source behavior, exposure risks, and migration issues before implementation work moves forward.

## Output Structure

Typical outputs:

```text
.reverse-spec/
  feature-inventory.md
  source-map.md
  assumptions.md
  scan-report.md
  validation-report.md
  export-report.md
  pipeline-report.md

specs/
  001-feature-name/
    spec.md
    reverse-analysis.md
    architecture-alignment.md
    security-considerations.md
    open-questions.md
    source-traceability.md
```

## Quality Gates

- Generated specs are draft reconstructed specs, not final truth.
- Validation should be clean enough before planning starts.
- Architecture review should happen before planning.
- Security audit should happen before planning.
- `/speckit.security-review.branch` should run only after implementation branch changes exist.

## Examples

### Laravel + Inertia + Vue

```bash
/speckit.reverse-spec.full-pipeline --source ../oss-repo --target "Laravel + Inertia + Vue"
```

### NestJS + React + PostgreSQL

```bash
/speckit.reverse-spec.extract --source ../oss-repo --target "NestJS + React + PostgreSQL" --features auth,billing --max-features 5
```

## Troubleshooting

- `extension command not found`: confirm the extension is installed and that the command starts with `/speckit.reverse-spec.`.
- `catalog install not available`: use the local development install or GitHub release zip until the extension is published to the configured catalog.
- Generated specs are too broad: narrow `--features`, reduce `--max-features`, and tighten the source scan scope.
- Missing `architecture_constitution.md`: provide the file path with `--constitution` or add the constitution file to the project.
- Source repo path invalid: verify the `--source` path or repository URL before running the pipeline.

## Validation

Run the repository validation check:

```bash
python3 -m pytest tests/test_extension_structure.py
```

## Catalog Publishing Notes

- Use `specify extension add --dev /path/to/spec-kit-reverse-spec` while developing locally.
- Use `specify extension add reverse-spec --from https://github.com/DyanGalih/spec-kit-reverse-spec/archive/refs/tags/v0.1.1.zip` for the GitHub release artifact.
- Use `specify extension add reverse-spec` only after the extension is present in the configured catalog.
- Keep the extension id stable as `reverse-spec` so catalog consumers and command references stay consistent.

## License

MIT
