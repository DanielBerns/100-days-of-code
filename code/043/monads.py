from typing import TypeVar, Generic

T = TypeVar('T')

class Maybe(Generic[T]):
    def __init__(self, value: Optional[T]) -> None:
        self._value: Optional[T] = value
        
    @property
    def value(self) -> Optional[T]:
        return self._value
    
    def bind(self, function: Callable[[T], T]) -> Maybe[T]:
        result = function(self.value) if self.value else None
        return Maybe(result)

    
