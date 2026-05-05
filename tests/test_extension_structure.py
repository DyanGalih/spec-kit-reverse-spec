from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_COMMAND_PREFIX = "speckit.reverse-spec."
REQUIRED_TEMPLATES = {
    "spec.template.md",
    "reverse-analysis.template.md",
    "architecture-alignment.template.md",
    "security-considerations.template.md",
    "source-traceability.template.md",
    "open-questions.template.md",
    "feature-inventory.template.md",
    "validation-report.template.md",
    "pipeline-report.template.md",
}
FORBIDDEN_COMMANDS = {
    "memory-hub.load",
    "memory-hub.save",
    "memory-md.load",
    "memory-md.save",
}


def read_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_extension_manifest_and_commands() -> None:
    manifest_path = ROOT / "extension.yml"
    assert manifest_path.is_file(), "extension.yml missing"

    manifest = read_yaml(manifest_path)

    assert manifest["extension"]["id"] == "reverse-spec"
    assert "provides" in manifest and "commands" in manifest["provides"]

    commands = manifest["provides"]["commands"]
    assert commands, "provides.commands missing or empty"

    for command in commands:
        assert command.get("name"), "command name missing"
        assert command.get("file"), "command file missing"
        assert command["name"].startswith(EXPECTED_COMMAND_PREFIX)

        command_path = ROOT / command["file"]
        assert command_path.is_file(), command_path
        assert command_path.read_text(encoding="utf-8").startswith("---\n"), command_path


def test_config_template_and_templates_exist() -> None:
    config_path = ROOT / "reverse-spec-config.template.yml"
    assert config_path.is_file(), "reverse-spec-config.template.yml missing"
    read_yaml(config_path)

    templates_dir = ROOT / "templates"
    assert templates_dir.is_dir(), "templates directory missing"

    for template_name in REQUIRED_TEMPLATES:
        assert (templates_dir / template_name).is_file(), template_name


def test_readme_is_present_and_safe() -> None:
    readme_path = ROOT / "README.md"
    assert readme_path.is_file(), "README.md missing"

    readme = readme_path.read_text(encoding="utf-8")

    for forbidden in FORBIDDEN_COMMANDS:
        assert forbidden not in readme, forbidden

    assert "/speckit.security-review.branch" in readme
    assert "after implementation changes" in readme


def test_templates_do_not_recommend_branch_before_implementation() -> None:
    templates_dir = ROOT / "templates"
    for path in templates_dir.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "/speckit.security-review.branch" in text:
            assert "only after implementation branch changes exist" in text
