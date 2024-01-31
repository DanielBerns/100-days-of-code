from typing import (Generator, Dict, Tuple)
from .base import Base

class Doc(Base):
    def __init__(self) -> None:
        super().__init__()
        self._attributes: Dict[str, str] = {}
        
    def add(self, key: str, value: str) -> None:
        self._attributes[key] = value
    
    def get(self, key: str, value: str) -> str:
        return self._attributes.get(key, value)
    
    def show(self) -> None:
        for key, value in self._attributes.items():
            print(f"{key:s}: {value:s}")

    def values(self) -> Generator[str, None, None]:
        for value in self._attributes.values():
            yield value

    def items(self) -> Generator[Tuple[str, str], None, None]:
        for key, value in self._attributes.items():
            yield key, value
