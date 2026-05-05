# Testing

The repository should keep lightweight validation coverage around the catalog-facing contract.

## Recommended Checks

- YAML parses for `extension.yml`.
- `extension.id` is `reverse-spec`.
- Every `provides.commands[*].file` exists.
- Every command file starts with YAML frontmatter.
- Every command name matches `speckit.reverse-spec.<command>`.
- `reverse-spec-config.template.yml` parses as YAML.
- README installation instructions match the supported installation paths.

## Current Validation Approach

The repository includes a manifest validation test in `tests/test_manifest.py` that checks the extension metadata, command files, config template, and README install instructions.

## Running Tests

Use your normal Python test runner for the repository. If `pytest` is available:

```bash
pytest
```
