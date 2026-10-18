# lml_common.immutable

A high-integrity utility module designed to enforce **true runtime constants** and immutable namespaces in Python. 

Unlike standard `typing.Final` annotations (which are bypassed at runtime) or `@dataclass(frozen=True)` (which only protects individual instances), this module prevents accidental or unauthorized mutations at **both the instance and the class level**.

---

## 🛠 Why This Exists (The Algorithmic Contract)

Python's dynamic nature is an asset, but "mutable constants" are an architectural hazard—especially when interfacing with hardware registries, device configurations, or fixed firmware endpoints. 

`lml_common.immutable` upgrades constants from a mere naming convention (`UPPERCASE_NAMES`) to an ironclad runtime guarantee. It supports two explicit, transparent enforcement models:
1. **The Python Metaclass Guard:** Lock down dynamic class structures immediately after configuration/decoration phases end.
2. **The Compiled Cython Extension Layer:** Compile configuration primitives straight to a native machine-level binary (`.so` / `.pyd`) for unbreakable runtime isolation.

---

## 🚀 Usage Guide

### 1. Pure Python Layout (Metaclass + Decorator)
This approach allows standard Python libraries (like `dataclasses`) to dynamically generate boilerplate logic during initialization, then locks the class down permanently.

```python
from dataclasses import dataclass
from lml_common import freeze_class, FrozenClassMeta

@freeze_class
@dataclass(frozen=True)
class NiUsb6009(metaclass=FrozenClassMeta):
    VID: int = 0x3923
    PID: int = 0x717b
    EP_CMD_OUT: int = 0x01
    EP_ACK_IN: int = 0x81
    EP_ANLG_IN: int = 0x82

# --- Enforced Behaviors ---

# 1. Reading works as normal:
print(f"0x{NiUsb6009.VID:04x}")  # Output: 0x3923

# 2. Modifying the Class raises a hard runtime crash:
NiUsb6009.VID = 0x1234  
# ❌ TypeError: Class 'NiUsb6009' is frozen. Cannot modify or append configuration constant 'VID'.

# 3. Modifying an Instance raises a hard runtime crash:
NI = NiUsb6009()
NI.VID = 0x1234  
# ❌ dataclasses.FrozenInstanceError: cannot assign to field 'VID'
```

### 2. Compiled Cython Layout (Native Immutability)
For maximum speed and machine-level memory safety, compile definitions straight to an extension structure. Fields declared `readonly` generate implicit C-getters for Python but omit the setters entirely.

```python
# Defined natively in immutable.pyx
import cython

@cython.cclass
class NativeHardwareConstants:
    VID: cython.int = cython.declare(cython.int, 0x3923, visibility='readonly')
    PID: cython.int = cython.declare(cython.int, 0x717b, visibility='readonly')

NI = NativeHardwareConstants()
```

```python
# Imported into your Python application
import lml_common.immutable as common

common.NI.VID = 0x1234
# ❌ AttributeError: attribute 'VID' of 'NativeHardwareConstants' objects is not writable
```

---

## 🔍 Deterministic vs. Opaque Magic

Unlike heavy enterprise framework environments (e.g., JVM/Gradle) that obscure execution flow using background reflection loops, dynamic aspect wrappers, or bytecode injection, `lml_common.immutable` values the **Algorithmic Contract**:
* **WYSIWYG:** Every object preserves its true identity (`id()`) and its exact runtime class constructor (`type()`). 
* **Zero Caching Artifacts:** No background build daemons, no implicit state dependencies, and no magic side-effects. 
* **Trivially Debuggable:** Illegal modifications crash instantly, pinpointing the precise line code responsible for the violation.

---

## 📦 Installation & Integration

To link this module into downstream hardware drivers or applications locally during development, install it inside your project's virtual environment in **Editable Mode**:

```bash
# Navigate to the root directory of your workspace containing pyproject.toml
cd lml_common/

# Install with development extensions 
pip install -e ".[dev]"
```

### Downstream Dependency Verification
When integrated properly with standard, declarative build systems, verification tools like `mypy` will catch constant assignments during your static linting phase before deployment:

```text
error: Cannot assign to final name "VID"  [misc]
```

