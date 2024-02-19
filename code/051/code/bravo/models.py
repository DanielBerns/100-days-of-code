@dataclass
class Definition:
    kind: str
    order: str
    family: str
    genus: str
    species: str


class Component:
    def __init__(self, definition: Definition, identifier: str) -> None:
        self._definition: Definition = definition
        self._identifier: str = identifier
 
    @property
    def definition(self) -> Definition:
        return self._definition
    
    @property
    def identifier(self) -> str:
        return self._identifier


class State(Protocol):
    def current_value(self) -> T
    def update(self, x: Percept) -> 'State':
        ...
        
class Result(Protocol):
    def evaluate(self, x: Percept, s: State) ->
class Node:
    pass

class Edge:

    
class Graph:
    def __init__(self):
        self._nodes: Dict[]
