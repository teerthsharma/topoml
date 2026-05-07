"""TopoML SDK — Unified Python SDK for topological machine learning.

Teerth Sharma's complete topological ML stack in one import:

    import topoml as tm

    # Physics: Faraday God Tensor (E×H coupling)
    tm.faraday.predict(geometry)

    # Physics: Hamilton N-body coupling tensor
    tm.hamilton.coupling(bodies)

    # Visualization: 3D persistent homology rendering
    tm.topo.render(barcodes)

    # Memory: Topological embedding store (FAISS + ripser)
    tm.phi.query("remember the physics discussion")

    # CLI tools
    tm.epsilon.stochastic()
    tm.seal.encrypt("secret")

Sub-packages (install with `pip install topoml[all]` for everything):
    faraday   — God Tensor (electromagnetics)
    hamilton  — N-body coupling tensor
    topoflow  — 3D PH visualization
    lambda-topo — TDA memory + manifold learning
    phi-mem   — LLM topological memory
    epsilon-cli — Stochastic resonance CLI
    seal-vault  — Quantum-seeded encryption

Version map:
    faraday  >= 0.1.0
    hamilton >= 0.1.0
    topoflow >= 0.1.0
    lambda-topo >= 0.2.0
    phi-mem  >= 0.1.0
    epsilon-cli >= 0.1.0
    sealvault >= 0.1.0
"""

__version__ = "0.1.0"

def _missing(pkg: str, extra: str) -> None:
    import importlib
    try:
        importlib.import_module(pkg)
    except ImportError:
        raise ImportError(
            f"topoml.{pkg!r} is not installed. "
            f"Install it with: pip install topoml[{extra!r}]"
        )

# ---------------------------------------------------------------------------
# Lazy import stubs — fail fast with actionable error messages
# ---------------------------------------------------------------------------

class _LazyModule:
    """Lazy import wrapper with helpful error on missing dependency."""
    def __init__(self, module_name: str, install_extra: str):
        self._module_name = module_name
        self._install_extra = install_extra
        self._mod = None

    def _load(self):
        if self._mod is None:
            _missing(self._module_name, self._install_extra)
            import importlib
            self._mod = importlib.import_module(self._module_name)
        return self._mod

    def __getattr__(self, name):
        return getattr(self._load(), name)

# Lazy-load subpackages so `import topoml as tm; tm.faraday` works
# without requiring all dependencies at import time.
try:
    import faraday
    faraday = faraday
except ImportError:
    faraday = _LazyModule("faraday", "physics")

try:
    import hamliton
    hamilton = hamliton
except ImportError:
    hamilton = _LazyModule("hamliton", "physics")

try:
    import topoflow
    topo = topoflow
except ImportError:
    topo = _LazyModule("topoflow", "viz")

try:
    import lambda_topo as _lt
    lambda_topo = _lt
except ImportError:
    lambda_topo = _LazyModule("lambda_topo", "memory")

try:
    import phi_mem as _pm
    phi_mem = _pm
except ImportError:
    phi_mem = _LazyModule("phi_mem", "memory")

try:
    import epsilon_cli as _ec
    epsilon = _ec
except ImportError:
    epsilon = _LazyModule("epsilon_cli", "tools")

try:
    import sealvault as _sv
    seal = _sv
except ImportError:
    seal = _LazyModule("sealvault", "crypto")