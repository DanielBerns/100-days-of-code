class Task:
    def __init__(self, name: str, level: int) -> None:
        self._name: str = name
        self._level: int = level
        self._state: int = 0
        self._
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def level(self) -> int:
        return self._level
    
    @property
    def state(self) -> int:
        return self._state
    
    @state.setter
    def state(self, value: int) -> None:
        self._state = value
        

    

