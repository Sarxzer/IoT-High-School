from _typeshed import Incomplete

_CONVERT: Incomplete
_RD_SCRATCH: Incomplete
_WR_SCRATCH: Incomplete

class DS18X20:
    ow: Incomplete
    buf: Incomplete
    def __init__(self, onewire) -> None: ...
    def scan(self): ...
    def convert_temp(self) -> None: ...
    def read_scratch(self, rom): ...
    def write_scratch(self, rom, buf) -> None: ...
    def read_temp(self, rom): ...
