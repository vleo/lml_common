from typing import Any, TypeVar

T = TypeVar('T')

class FrozenClassMeta(type):
    """Metaclass that permanently locks down class-level configuration attributes
    once the complete setup phase has finished.
    """
    def __new__(mcs, name: str, bases: tuple[type, ...], attrs: dict[str, Any]) -> type:
        cls = super().__new__(mcs, name, bases, attrs)
        setattr(cls, '_locked', False)
        return cls

    def __setattr__(cls, name: str, value: Any) -> None:
        if getattr(cls, '_locked', False):
            raise TypeError(
                f"Class '{cls.__name__}' is frozen. "
                f"Cannot modify or append configuration constant '{name}'."
            )
        super().__setattr__(name, value)

def freeze_class(cls: T) -> T:
    """Class decorator that locks down the metaclass state after all adjacent
    class decorators (like @dataclass) complete their modification routines.
    """
    setattr(cls, '_locked', True)
    return cls
