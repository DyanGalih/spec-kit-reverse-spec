# Command: /speckit.reverse-spec.map

Map source architecture to the target stack architecture.

## Arguments
--target (required): The target stack/architecture pattern.
--constitution (default: architecture_constitution.md): Reference for architectural rules.

## Behavior
1. Analyze source code patterns against target stack conventions.
2. Generate `architecture-alignment.md` in each feature spec directory.
3. Include:
   - Layer mapping
   - Boundaries
   - Drift detection
   - Target stack alignment
