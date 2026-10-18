# tests/test_both.py
from dataclasses import dataclass
from lml_common.immutable import FrozenClassMeta, freeze_class

# 1. Test the Pure Python Metaclass Module
@freeze_class
@dataclass(frozen=True)
class PurePythonConfig(metaclass=FrozenClassMeta):
    VID: int = 0x3923

print("--- Testing Pure Python Immutability ---")
print(f"Reading VID: 0x{PurePythonConfig.VID:04x}")

try:
    PurePythonConfig.VID = 0x1234
    print("❌ Error: Pure Python mutation allowed!")
except TypeError as e:
    print(f"✅ Success (Caught expected crash): {e}")


# 2. Test the Compiled Cython Binary Module
from lml_common import CONST

print("\n--- Testing Compiled Cython Immutability ---")
print(f"Reading VID: 0x{CONST.VID:04x}")

try:
    CONST.VID = 0x1234
    print("❌ Error: Cython binary mutation allowed!")
except AttributeError as e:
    print(f"✅ Success (Caught expected crash): {e}")
