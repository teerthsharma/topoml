# TopoML SDK

Unified Python SDK for Teerth Sharma's topological ML stack.

## Install

```bash
# Full stack
pip install topoml[all]

# Just physics
pip install topoml[physics]

# Just visualization
pip install topoml[viz]
```

## Modules

| Module | Package | What it does |
|--------|---------|-------------|
| `topoml.faraday` | faraday | God Tensor: E×H electromagnetic coupling |
| `topoml.hamilton` | hamilton | N-body EM coupling tensor |
| `topoml.topo` | topoflow | 3D persistent homology visualization |
| `topoml.lambda_topo` | lambda_topo | TDA memory + manifold learning |
| `topoml.phi_mem` | phi-mem | LLM topological memory |
| `topoml.epsilon` | epsilon-cli | Stochastic resonance CLI |
| `topoml.seal` | sealvault | Quantum-seeded encryption |

## Quick Start

```python
import topoml as tm

# God Tensor: predict EM field topology
# tm.faraday.predict(geometry)  # requires faraday installed

# Hamilton: N-body coupling
# tm.hamilton.coupling(bodies)  # requires hamilton installed

# TopoFlow: render persistent homology
# tm.topo.render(barcodes)  # requires topoflow installed
```

## CLI Tools

After installing `topoml[all]` or `topoml[tools]`:
- `faraday-predict`, `faraday-demo`
- `hamliton train`, `hamliton score`
- `topoflow render`, `topoflow demo`
- `lambda-topo-manifold`
- `phi-mem add`, `phi-mem query`
- `epsilon-stochastic`
- `sealvault encrypt`

## Your Stack

These tools were built by Teerth Sharma (github.com/teerthsharma):
- **Physics moat:** Banach fixed-point EM coupling (no FDFD at prediction time)
- **Topology moat:** Persistent homology as a universal geometry descriptor
- **Memory moat:** Topological signatures for LLM context, not raw embeddings
- **Systems moat:** Stochastic resonance + quantum-seeded crypto

## License

MIT