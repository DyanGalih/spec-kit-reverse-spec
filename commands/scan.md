# Command: /speckit.reverse-spec.scan

Scan the source repository for feature patterns and structure.

## Arguments
--source (required): Path to the source repository.
--output (default: .reverse-spec): Output directory for scan results.

## Behavior
1. Analyze directory structure and entry points.
2. Identify core modules/features based on code patterns.
3. Generate `.reverse-spec/feature-inventory.md`.
4. Generate `.reverse-spec/source-map.md`.
5. Generate `.reverse-spec/assumptions.md`.
6. Generate `.reverse-spec/scan-report.md`.
