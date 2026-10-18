from .immutable import FrozenClassMeta, freeze_class

try:
    # Expose the compiled constants cleanly if called from the package root
    from .lmlconstants import CONSTANTS as CONST
except ImportError:
    # Fallback/warning handle if developers forget to compile via pip
    CONST = None

__all__ = ["FrozenClassMeta", "freeze_class", "CONST"]

