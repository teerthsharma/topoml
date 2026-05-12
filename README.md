# TopoML SDK

**Version 0.1.0** · Python ≥ 3.10 · [GitHub](https://github.com/teerthsharma/topoml)

---

## Overview

TopoML is a unified Python SDK encapsulating Teerth Sharma's topological machine learning stack. It provides composable interfaces across four scientific domains — electromagnetic physics, topological data analysis, long-context memory, and secure computation — as a single pip-installable package with optional modular dependencies.

The SDK is structured around a **layered architecture**:

```
┌─────────────────────────────────────────────┐
│              topoml (meta-package)           │
├──────────────┬──────────────┬────────────────┤
│   Physics    │  Topology    │    Systems     │
│  ──────────  │  ──────────  │  ────────────  │
│  faraday     │  topoflow    │  epsilon-cli   │
│  hamliton    │  lambda_topo │  sealvault     │
│              │  phi_mem     │                │
└──────────────┴──────────────┴────────────────┘
```

---

## Installation

TopoML supports granular dependency installation so researchers can provision only the components relevant to their workflow.

```bash
# Full stack — all modules and CLI tools
pip install topoml[all]

# Physics layer only — faraday + hamliton
pip install topoml[physics]

# Visualization layer only — topoflow + lambda_topo
pip install topoml[viz]

# Memory layer only — phi_mem + lambda_topo
pip install topoml[memory]

# Cryptographic layer — sealvault
pip install topoml[crypto]

# CLI tools standalone
pip install topoml[tools]
```

---

## Module Reference

### Physics Layer

#### `topoml.faraday` — God Tensor (Electromagnetic Coupling)

**Package:** `faraday >= 0.1.0`

The **God Tensor** implements a Banach fixed-point formulation of the electromagnetic cross product coupling **E × H**, enabling field topology prediction at prediction time without requiring finite-difference time-domain (FDFD) simulation.

```python
import topoml as tm

# Predict EM field topology from a geometric input
prediction = tm.faraday.predict(geometry)
```

**Key properties:**
- Banach fixed-point convergence guarantees
- No FDFD required at inference
- E×H coupling as the core operator

---

#### `topoml.hamilton` — N-Body Coupling Tensor

**Package:** `hamliton >= 0.1.0`

The **N-body coupling tensor** generalizes pairwise electromagnetic interactions to arbitrary many-body systems, encoding multi-body coupling strengths in a single rank-N tensor structure.

```python
import topoml as tm

# Compute N-body coupling tensor
coupling = tm.hamilton.coupling(bodies)
```

**Key properties:**
- Generalizes pairwise EM coupling to N bodies
- Tensor-structured coupling coefficients
- Suitable for structured many-body simulation

---

### Topology Layer

#### `topoml.topo` — Persistent Homology Visualization

**Package:** `topoflow >= 0.1.0`

**TopoFlow** renders 3D persistent homology barcodes and diagrams, providing interactive visualization of topological features across filtration scales. Persistent homology detects connected components (H₀), holes (H₁), voids (H₂), and higher-dimensional topological invariants.

```python
import topoml as tm

# Render a persistence barcode or diagram in 3D
tm.topo.render(barcodes)
```

**Key properties:**
- 3D interactive rendering of PH barcodes
- Multi-dimensional homology support (H₀, H₁, H₂, …)
- Filtration-scale axis for topological feature persistence

**CLI tools:**

```bash
topoflow render   # Render PH diagram from file
topoflow demo     # Run demonstration with synthetic data
```

---

#### `topoml.lambda_topo` — TDA Memory & Manifold Learning

**Package:** `lambda-topo >= 0.2.0`

Combines persistent homology analysis with manifold learning techniques. Provides tools for extracting topological signatures from high-dimensional datasets and learning low-dimensional manifold structure informed by topological priors.

```bash
lambda-topo-manifold   # CLI for manifold learning with TDA priors
```

**Key properties:**
- Persistent homology as a universal geometry descriptor
- Topological feature extraction for downstream ML tasks
- Manifold structure learning with topological constraints

---

### Memory Layer

#### `topoml.phi_mem` — LLM Topological Memory

**Package:** `phi-mem >= 0.1.0`

**phi-mem** provides a topological memory store for large language models. Rather than relying on raw embedding vectors, it encodes context using topological signatures (e.g., persistence diagrams, Betti sequences), enabling richer structural memory retrieval.

```python
import topoml as tm

# Store a topological embedding
tm.phi_mem.add(document, embedding_type="diagram")

# Query the topological memory store
results = tm.phi_mem.query("retrieve physics discussion")
```

**Key properties:**
- Topological signatures as memory tokens (not raw embeddings)
- FAISS-backed approximate nearest-neighbor retrieval
- Ripser-compatible diagram computation

**CLI tools:**

```bash
phi-mem add    # Add document to topological memory
phi-mem query  # Query the memory store
```

---

### Systems Layer

#### `topoml.epsilon` — Stochastic Resonance CLI

**Package:** `epsilon-cli >= 0.1.0`

Implements **stochastic resonance** — a phenomenon where system noise enhances weak signal transmission. The epsilon-cli provides a command-line interface for configuring and running stochastic resonance experiments on arbitrary signal inputs.

```bash
epsilon-stochastic --signal <input> --noise-level <sigma>
```

---

#### `topoml.seal` — Quantum-Seeded Encryption

**Package:** `sealvault >= 0.1.0`

Provides quantum-seeded encryption primitives for securing topological signatures and model artifacts. Uses quantum entropy sources to seed cryptographically secure random number generators.

```python
import topoml as tm

# Encrypt a payload with quantum-seeded key material
ciphertext = tm.seal.encrypt(plaintext)
```

**CLI tools:**

```bash
sealvault encrypt   # Encrypt with quantum-seeded key derivation
sealvault decrypt   # Decrypt sealed payloads
```

---

## Quick Start

```python
import topoml as tm

# ── Physics: EM field topology prediction ──────────────────────────────
# Requires: pip install topoml[physics]
field_topology = tm.faraday.predict(geometry)

# ── Physics: N-body coupling tensor ────────────────────────────────────
# Requires: pip install topoml[physics]
coupling_tensor = tm.hamilton.coupling(bodies)

# ── Topology: Render persistent homology ───────────────────────────────
# Requires: pip install topoml[viz]
tm.topo.render(persistence_barcodes)

# ── Memory: Topological LLM memory store ───────────────────────────────
# Requires: pip install topoml[memory]
tm.phi_mem.add("electromagnetic topology discussion", content)
context = tm.phi_mem.query("EM topology")

# ── Systems: Quantum-seeded encryption ──────────────────────────────────
# Requires: pip install topoml[crypto]
secret = tm.seal.encrypt("topological model weights")
```

---

## Version Map

| Sub-package | Package name | Minimum Version |
|-------------|--------------|-----------------|
| faraday | `faraday` | ≥ 0.1.0 |
| hamilton | `hamliton` | ≥ 0.1.0 |
| topoflow | `topoflow` | ≥ 0.1.0 |
| lambda_topo | `lambda-topo` | ≥ 0.2.0 |
| phi_mem | `phi-mem` | ≥ 0.1.0 |
| epsilon | `epsilon-cli` | ≥ 0.1.0 |
| seal | `sealvault` | ≥ 0.1.0 |

---

## Architecture & Design Principles

### Physics Moat: Banach Fixed-Point EM Coupling

The Faraday and Hamilton modules exploit Banach fixed-point convergence to solve electromagnetic coupling equations without iterative FDFD simulation at prediction time. This separates the expensive physics solve (training/inference setup) from fast topological prediction, yielding constant-time inference after a single fixed-point convergence.

### Topology Moat: Persistent Homology as Universal Geometry Descriptor

Persistent homology (PH) provides a dimension-agnostic description of geometric and algebraic structure. Unlike raw point clouds or embedding vectors, PH is:

- **Stable** — small perturbations in input produce small perturbations in output
- **Multi-scale** — captures structure across all filtration scales simultaneously
- **Coordinate-free** — invariant to rigid motions and ambient dimension

### Memory Moat: Topological Signatures for LLM Context

Storing raw embedding vectors in LLM context windows is both high-dimensional and semantically lossy. Topological memory encodes context as PH-derived signatures (barcodes, Betti curves, persistence images), preserving structural relationships rather than raw coordinate proximity.

### Systems Moat: Stochastic Resonance + Quantum-Seeded Crypto

Stochastic resonance allows weak topological signals to be amplified via controlled noise injection — useful for signal extraction from sparse PH data. Quantum-seeded encryption ensures that cryptographic key material for securing models and data is sourced from quantum entropy, future-proofing against classical and quantum adversaries.

---

## License

MIT — Teerth Sharma ([github.com/teerthsharma](https://github.com/teerthsharma))
