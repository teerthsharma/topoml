# Contributing to TopoML

Thank you for contributing to TopoML.

## Development Setup

```bash
git clone https://github.com/teerthsharma/topoml.git
cd topoml
python -m pip install -e ".[dev]"
```

## Running Tests

```bash
# All tests
python -m pytest tests/ -v

# With coverage
python -m pytest tests/ -v --cov=topoml --cov-report=term-missing
```

## Code Quality

```bash
# Lint
ruff check src/

# Format check
ruff format --check src/

# Type check
mypy src/ --ignore-missing-imports
```

## Project Structure

```
topoml/
├── src/
│   └── topoml/         # SDK modules
├── tests/              # Test suite
└── pyproject.toml
```