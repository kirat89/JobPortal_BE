# 📘 Developer Documentation

## 🛠 Project Setup Overview

This document outlines the development environment setup, tooling, and workflows used in the project.

---

## 📁 Dev Requirements

### 📄 `dev-requirements.txt`

This file lists all development dependencies needed to maintain code quality and consistency:

```txt
black==24.4.2
flake8==7.0.0
isort==5.13.2
mypy==1.10.0
pre-commit==3.7.0
```

### Purpose of Each Tool:

* **black**: Auto-formats Python code for consistency.
* **flake8**: Linter that checks for code style and errors.
* **isort**: Automatically sorts imports.
* **mypy**: Static type checker for Python.
* **pre-commit**: Git hook manager that runs the above tools before each commit.

---

## 🧱 Configuration Files

### 📄 `.flake8`

```ini
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = .git,__pycache__,.venv,venv,env,migrations
```

### 📄 `mypy.ini`

```ini
[mypy]
plugins = sqlalchemy.ext.mypy.plugin
ignore_missing_imports = True
disallow_untyped_defs = True
check_untyped_defs = True
strict_optional = True
exclude = migrations|tests
```

### 📄 `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.4.2
    hooks:
      - id: black

  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.10.0
    hooks:
      - id: mypy

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
```

---

## ⚙️ Development Setup Steps

1. **Clone the project**
2. **Create virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dev dependencies**

```bash
pip install -r dev-requirements.txt
```

4. **Create the config files listed above**
5. **Install pre-commit hooks**

```bash
pre-commit install
```

6. **Run checks on all files**

```bash
pre-commit run --all-files
```

---

## 🔄 Workflow for Making Changes

1. Write or modify code.

2. Stage changes with Git.

3. Commit changes:

   * Pre-commit will auto-run checks (black, flake8, isort, mypy).
   * If any check fails, the commit will be blocked.
   * Fix issues, re-add the files, and commit again.

4. Optional: Run tools manually for feedback

```bash
black .
flake8 .
isort .
mypy .
```

---

## 🧠 Why This Setup Matters

* Ensures clean, consistent, type-safe code.
* Catches bugs early (even before running the code).
* Saves time during reviews and debugging.
* Makes team collaboration smooth and predictable.

---

FastAPI project structure.

app/main.py — Entry point, create FastAPI instance, include routers.

app/config.py — Load config from environment or defaults.

app/database.py — Setup SQLAlchemy engine and sessionmaker.

app/models/ — DB tables defined as Python classes.

app/schemas/ — Pydantic models for validation and serialization.

app/crud/ — Functions for database operations to keep business logic clean.

app/api/ — FastAPI routers grouped by resource.

app/core/ — Security, utilities, and helpers.

app/tests/ — Automated tests, ideally using pytest.

alembic/ — Database migration scripts.

env and config files — For environment variables and tooling.
