# 🔄 Reverse Spec Kit

> Reverse-engineer existing OSS repositories into Spec Kit-compatible feature specifications for rebuilding in a different target stack.

[![Version](https://img.shields.io/badge/version-0.1.0-22c55e)](extension.yml)
[![Spec Kit](https://img.shields.io/badge/Spec%20Kit-compatible-2563eb)](https://spec-kit.dev)
[![Role](https://img.shields.io/badge/role-reverse--engineering-blue)](https://spec-kit.dev)

---

# What Is This?

Reverse Spec Kit is a specialized extension designed to bridge the gap between legacy or open-source repositories and modern Spec Kit workflows.

It automates the process of extracting **pure behavioral logic** from codebases, mapping it to your project's architecture standards, and generating implementation-ready feature specifications.

---

# The Problem It Solves

When rebuilding or migrating applications, developers often struggle with:

* **Hidden Logic**: Business rules buried deep within framework-specific implementations.
* **Architectural Mismatch**: Difficulty mapping legacy patterns to a new target stack.
* **Loss of Context**: Missing the "why" behind existing code during manual extraction.
* **Drift**: Introducing inconsistencies when translating logic from one stack to another.

Reverse Spec Kit treats the source repository as the "Source of Truth" for behavior, extracting it into structured Spec Kit artifacts (`specs/`) while ensuring alignment with your new architecture.

---

# What It Actually Does

| Phase          | What Happens                                                | Output                                         |
| -------------- | ----------------------------------------------------------- | ---------------------------------------------- |
| **Scan**       | Analyzes source structure and identifies feature patterns   | Feature inventory and source maps              |
| **Extract**    | Converts source code logic into behavioral specifications   | `specs/NNN-feature/spec.md`                    |
| **Map**        | Aligns extracted logic with the target stack architecture   | `architecture-alignment.md`                    |
| **Security**   | Identifies security controls and threat surfaces in source  | `security-considerations.md`                   |
| **Validate**   | Checks for completeness, ambiguities, and blockers          | Validation reports and status assignments      |
| **Export**     | Finalizes the specification suite for implementation        | Pipeline and export reports                    |

---

# Key Philosophy: Behavior Over Implementation

Reverse Spec Kit follows a strict rule: **Extract what it does, not how it does it.**

The goal is to generate specifications that define *requirements* and *logic*, allowing the AI (via Spec Kit) to implement them correctly in the target stack without being biased by legacy implementation details.

---

# Integration Workflow

Reverse Spec Kit is designed to orchestrate governance across the Spec Kit ecosystem:

1. **Memory Synthesis**: Uses `memory-md` to bootstrap the project context and plan the reverse-engineering strategy.
2. **Reverse Pipeline**: Orchestrates scan, extraction, and mapping.
3. **Architecture Guard**: Validates that the "Map" results align with your `architecture_constitution.md`.
4. **Security Review**: Reviews extracted security considerations for the new stack.

---

# Quick Start

## 1. Install

```bash
cd /path/to/spec-kit-project
specify extension add reverse-spec
```

---

## 2. Configure

Initialize the `reverse-spec-config.template.yml` to define your source repo and target stack.

---

## 3. Run the Pipeline

```bash
/speckit.reverse-spec.full-pipeline --source <repo> --target "<stack>"
```

---

# Commands

| Command         | Purpose                                                                 |
| --------------- | ----------------------------------------------------------------------- |
| `full-pipeline` | **Orchestrator**. Runs the complete reverse-spec workflow end-to-end.    |
| `scan`          | Scans the source repository for features and architecture patterns.     |
| `extract`       | Extracts logic into `specs/` using behavioral templates.                |
| `map`           | Maps source logic to target stack architecture.                        |
| `validate`      | Reviews extracted specs for completeness and alignment.                 |
| `export`        | Generates final pipeline reports and exports the specification suite.   |

---

# Quality Gates

After running the pipeline, the extension provides the exact next commands to transition to delivery:

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

---

# Installation

## Registry Installation

```bash
cd /path/to/spec-kit-project
specify extension add reverse-spec
```

## GitHub Installation

```bash
cd /path/to/spec-kit-project
specify extension add reverse-spec --from \
  https://github.com/DyanGalih/spec-kit-reverse-spec/archive/refs/tags/v0.1.0.zip
```

---

# Relationship to Other Extensions

| Extension          | Responsibility                                           |
| ------------------ | -------------------------------------------------------- |
| **Reverse Spec**   | **Extraction**. Source logic → Spec Kit specifications.  |
| **Memory Hub**     | **Context**. Durable project memory and historical sync. |
| **Arch Guard**     | **Governance**. Alignment with target architecture.     |
| **Security Review**| **Validation**. Security auditing of specs and code.     |

---

# Working with Existing Projects

If you are running Reverse Spec Kit on a project that has already been started or uses a specific framework standard:

1. **Architecture Alignment**: The `/speckit.reverse-spec.map` command will prioritize your existing `architecture_constitution.md` to ensure extracted logic is mapped to your current project's patterns.
2. **Incremental Porting**: You can target specific features using the `--features` argument to avoid scanning the entire source repo.
3. **Gap Analysis**: Use the generated `specs/` to identify logic that hasn't been implemented in your new stack yet.

---

# Example Usage

## Scenario: Rebuilding a Legacy Express.js API in NestJS

To reverse-engineer a legacy application and prepare it for a new stack, follow this standard execution:

### 1. Preflight
Ensure your project is initialized with Spec Kit and required extensions.

### 2. Execution
Run the full pipeline to scan the source repository and generate specifications.

```bash
# Using a remote repository
/speckit.reverse-spec.full-pipeline \
  --source "https://github.com/DyanGalih/legacy-express-api" \
  --target "NestJS + PostgreSQL" \
  --mode "review-ready"

# OR using a local path
/speckit.reverse-spec.full-pipeline \
  --source "./legacy-projects/express-api" \
  --target "NestJS + PostgreSQL"
```

### 3. Review Generated Artifacts
The pipeline will generate a complete specification suite in the `specs/` directory:

```text
specs/
  001-user-authentication/
    spec.md
    reverse-analysis.md
    architecture-alignment.md
    security-considerations.md
    source-traceability.md
  002-order-processing/
    ...
```

### 4. Transition to Delivery
Once the specs are validated, continue with the Spec Kit delivery workflow:

```bash
/speckit.architecture-guard.architecture-review
/speckit.plan
/speckit.tasks
/speckit.implementation
```

---

# License

[MIT](LICENSE) © [DyanGalih](https://github.com/DyanGalih)

