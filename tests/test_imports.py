"""Smoke tests for TopoML imports."""

import pytest


def test_import_faraday():
    """Verify faraday submodule imports."""
    try:
        from topoml import faraday  # noqa: F401
    except ImportError:
        pytest.skip("faraday not installed")


def test_import_hamilton():
    """Verify hamilton submodule imports."""
    try:
        from topoml import hamilton  # noqa: F401
    except ImportError:
        pytest.skip("hamilton not installed")


def test_import_topo():
    """Verify topo submodule imports."""
    try:
        from topoml import topo  # noqa: F401
    except ImportError:
        pytest.skip("topo not installed")


def test_import_lambda_topo():
    """Verify lambda_topo submodule imports."""
    try:
        from topoml import lambda_topo  # noqa: F401
    except ImportError:
        pytest.skip("lambda_topo not installed")


def test_import_phi_mem():
    """Verify phi_mem submodule imports."""
    try:
        from topoml import phi_mem  # noqa: F401
    except ImportError:
        pytest.skip("phi_mem not installed")


def test_import_epsilon():
    """Verify epsilon submodule imports."""
    try:
        from topoml import epsilon  # noqa: F401
    except ImportError:
        pytest.skip("epsilon not installed")


def test_import_seal():
    """Verify seal submodule imports."""
    try:
        from topoml import seal  # noqa: F401
    except ImportError:
        pytest.skip("seal not installed")
