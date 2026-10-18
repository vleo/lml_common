# src/lml_common/xyzzyconsts.pyi
from typing import Final

class LMLCONSTS:
    # We tell the IDE these are Final/Read-only primitive integers
    VID: Final[int]
    PID: Final[int]
    EP_CMD_OUT: Final[int]
    EP_ACK_IN: Final[int]
    EP_ANLG_IN: Final[int]

# Expose the global instance signature exactly as it is initialized
CONSTANTS: LMLCONSTS
