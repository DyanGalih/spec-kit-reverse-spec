# Command: /speckit.reverse-spec.extract

Extract feature behavior and logic into specification templates.

## Arguments
--source (required): Path to the source repository.
--features (default: all): Specific features to extract.
--max-features: Limit the number of features extracted.

## Behavior
1. For each identified feature:
   - Create `specs/NNN-[feature-name]/`.
   - Populate `spec.md` using `spec.template.md`.
   - Populate `reverse-analysis.md` using `reverse-analysis.template.md`.
   - Populate `open-questions.md` using `open-questions.template.md`.
   - Populate `source-traceability.md` using `source-traceability.template.md`.
2. **Rule:** Write behavior, NOT implementation.
