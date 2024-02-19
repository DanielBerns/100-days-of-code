class Base:
    def __init__(self) -> None:
        self._ok: bool = True
        self._error: str = ""

    @property
    def ok(self) -> bool:
        return self._ok

    @ok.setter
    def ok(self, value: bool) -> None:
        self._ok = value

    @property
    def error(self) -> str:
        return self._error

    @error.setter
    def error(self, value: str) -> None:
        if value:
            self._error = value
            self.ok = False
