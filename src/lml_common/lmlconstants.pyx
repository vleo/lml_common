import cython

@cython.cclass
class LMLCONSTS:
    """A compiled C-extension configuration block.
    Attributes are fully exposed to Python for reading, but completely
    immutable from Python at runtime.
    """
    VID: cython.int = 0x3923
    PID: cython.int =  0x717b
    EP_CMD_OUT: cython.int = 0x01
    EP_ACK_IN: cython.int =  0x81
    EP_DGTL_IN: cython.int =  0x81
    EP_ANLG_IN: cython.int = 0x82

# Instantiate a single global instance to serve as the configuration block
CONSTANTS = LMLCONSTS()
