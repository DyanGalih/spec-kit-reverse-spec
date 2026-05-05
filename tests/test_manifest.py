from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def read_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_extension_manifest_is_valid_yaml_and_has_expected_id() -> None:
    manifest = read_yaml(ROOT / "extension.yml")

    assert manifest["schema_version"] == "1.0"
    assert manifest["extension"]["id"] == "reverse-spec"
    assert manifest["extension"]["version"] == "0.1.1"


def test_all_provided_command_files_exist() -> None:
    manifest = read_yaml(ROOT / "extension.yml")

    for command in manifest["provides"]["commands"]:
        assert (ROOT / command["file"]).is_file(), command["file"]


def test_all_command_files_have_frontmatter_and_matching_names() -> None:
    manifest = read_yaml(ROOT / "extension.yml")

    for command in manifest["provides"]["commands"]:
        path = ROOT / command["file"]
        text = path.read_text(encoding="utf-8")
        assert text.startswith("---\n"), path
        assert f'# Command: /{command["name"]}' in text, path


def test_config_template_parses_as_yaml() -> None:
    config = read_yaml(ROOT / "reverse-spec-config.template.yml")

    assert config["source"]["type"] == "local"
    assert config["output"]["work_dir"] == ".reverse-spec"
    assert config["pipeline"]["mode"] == "draft"


def test_readme_contains_supported_install_instructions() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "specify extension add --dev /path/to/spec-kit-reverse-spec" in readme
    assert "specify extension add reverse-spec --from https://github.com/DyanGalih/spec-kit-reverse-spec/archive/refs/tags/v0.1.1.zip" in readme
    assert "Only use:" in readme
    assert "specify extension add reverse-spec" in readme
