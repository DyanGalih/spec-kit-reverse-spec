# Reverse Spec Kit

Reverse Spec Kit is a Spec Kit extension for reverse-engineering existing OSS repositories into draft, Spec Kit-compatible feature specifications for a target-stack rebuild.

It is designed for migration and modernization work where the source repository is useful as behavioral evidence, but the rebuilt system should still be planned with Spec Kit conventions, review gates, and architecture governance.

## What It Does

- Scans a source repository and inventories likely product features.
- Extracts draft feature specs from observed source behavior.
- Maps source components to a target architecture and architecture constitution.
- Validates generated feature folders for traceability and readiness.
- Exports reports that hand off to memory, architecture, security, planning, and implementation workflows.

## What It Does Not Do

- It does not auto-implement the rebuilt system.
- It does not treat generated specs as final truth.
- It does not auto-run `speckit.security-review.branch`.
- It does not silently preserve the source architecture.
- It does not replace product review, architecture review, or security review.

## Installation

Install locally for development:

```bash
specify extension add --dev /path/to/spec-kit-reverse-spec
```

Install from GitHub release:

```bash
specify extension add reverse-spec --from https://github.com/DyanGalih/spec-kit-reverse-spec/archive/refs/tags/v0.1.1.zip
```

Only use:

```bash
specify extension add reverse-spec
```

when the extension is already available in the configured catalog.

## Command Reference

| Command | Purpose |
| --- | --- |
| `/speckit.reverse-spec.scan` | Scan a source repository and build a feature inventory. |
| `/speckit.reverse-spec.extract` | Generate draft reconstructed feature specs. |
| `/speckit.reverse-spec.map` | Map source architecture to the target stack and constitution. |
| `/speckit.reverse-spec.validate` | Validate generated feature folders and readiness. |
| `/speckit.reverse-spec.export` | Finalize specs and produce export reports. |
| `/speckit.reverse-spec.full-pipeline` | Orchestrate the full reverse-spec workflow without autopilot. |

## Full Pipeline

Run the pipeline when you want a complete reverse-engineering pass from source inventory to export reports:

```bash
/speckit.reverse-spec.full-pipeline --source ./legacy-app --target "NestJS + PostgreSQL" --mode review-ready
```

The pipeline stays in draft/review mode. It recommends follow-up governance commands, but it does not implement the feature set for you.

## Output Structure

Typical outputs look like this:

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

Reverse Spec Kit assumes these review gates are part of the handoff:

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

## Integration With Memory-MD

`memory-md` is used to preserve assumptions, source findings, and migration context across the reverse-spec workflow.

- Recommended before pipeline work: `/speckit.memory-md.plan-with-memory`
- Recommended after artifact generation: `/speckit.memory-md.capture`
- Recommended after implementation changes exist: `/speckit.memory-md.capture-from-diff`

## Integration With Architecture-Guard

`architecture-guard` helps keep reconstructed specs aligned to the target architecture instead of the source implementation.

- Use `/speckit.architecture-guard.architecture-review` after map and validate.
- Use governed planning and implementation commands only once the spec set is ready for delivery.

## Integration With Security-Review

`security-review` helps evaluate source behavior, exposed surfaces, and migration risks before implementation.

- Use `/speckit.security-review.audit` before planning.
- Use `/speckit.security-review.branch` only after implementation branch changes exist.
- Do not treat the reverse-spec export as a security sign-off.

## Examples

Reverse-engineer a local repository:

```bash
/speckit.reverse-spec.full-pipeline --source ./legacy-app --target "React + Node" --features all --mode draft
```

Focus on a limited feature set:

```bash
/speckit.reverse-spec.extract --source ./legacy-app --target "Next.js + PostgreSQL" --features auth,billing --max-features 3
```

Run mapping with a constitution file:

```bash
/speckit.reverse-spec.map --target "NestJS + PostgreSQL" --constitution architecture_constitution.md --source ./legacy-app
```

## Limitations

- Confidence is only as strong as the evidence in routes, tests, docs, and source structure.
- Low-confidence features may require manual product review.
- Architecture drift is reported, not repaired automatically.
- Generated specs are drafts and must be validated before planning.

## Troubleshooting

- If scanning finds too much infrastructure noise, tighten `--exclude` patterns and lower `--depth`.
- If extraction yields vague features, include tests and docs in the scan.
- If validation reports blocking questions, resolve them before planning.
- If the target stack cannot be inferred, provide `--target` explicitly.

## Catalog Publishing Notes

- Keep the extension id as `reverse-spec`.
- Keep the command names stable.
- Version this release as `0.1.1`.
- Ship the manifest, command docs, templates, config template, docs, and validation test together.
- Catalog consumers should install via the release zip once the extension is published.

## License

MIT
