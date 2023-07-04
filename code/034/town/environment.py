class Place:
    def __init__(self, name: str, kind: str, x: int, y: int, z: int):
        self._name = name
        self._kind = kind
        self._ubication = (x, y, z)        
        self._weather = {}

class Engine:
    def __init__(self):
        pass
    
    def update(self, place: Place) -> None:
        pass
    
class Weather(Engine):
    def __init__(self):
        super().__init__()
        
class Time(Engine):
    def __init__(self):
        super().__init__()
    
    
        
    
