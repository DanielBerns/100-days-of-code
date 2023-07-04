from typing import Dict, List


class State(Protocol):
    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass
    
    def update(self, perception: Dict[str, str]) -> None:
        pass

    
class Actor(Protocol):
    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass
    
    def update(self, state: State, perception: Dict[str, str]) -> None:
        pass


class Mind:
    def __init__(self, state: State, actor: Actor) -> None:
        self._state = state
        self._actor = actor

    @property
    def state(self) -> State:
        return self._state
    
    @property
    def actor(self) -> Actor:
        return self._actor

    def start(self):
        self.actor.start()        
        self.state.start()
        
    def update(self, perception: Dict[str, str]) -> None:
        self.actor.update(self.state, perception)
        self.state.update(perception)

    def stop(self):
        self.state.stop()
        self.actor.stop()
