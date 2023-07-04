from typing import Dict, Tuple

        
class PlaceException(Exception):
    pass

# https://www.redblobgames.com/grids/hexagons/#basics

class Place:
    def __init__(self, alpha: int, bravo: int):
        self._coordinates = (alpha, bravo, - alpha - bravo)
    
    @property
    def coordinates(self) -> Tuple[int, int, int]:
        return self._coordinates
    
    @coordinates.setter
    def coordinates(self, value: Tuple[int, int, int]) -> None:
        if len(value) == 3 and sum(value) == 0:
            self._coordinates = value
        else:
            raise PlaceException(f"invalid coordinates {str(value):s}")
            
    @property
    def invariant(self) -> bool:
        return sum(self.coordinates) == 0

    @property
    def radii(self) -> int:
        return max(abs(v) for v in self.coordinates)
    

class AllThesePlacesException(Exception):
    pass
    
class AllThesePlaces:
    def __init__(self) -> None:
        self._catalog = {}

    @property
    def catalog(self) -> Dict:
        return self._catalog
    
    def add_place(self, place: Place) -> None:
        try:
            a_place = self.catalog[place.coordinates]
        except KeyError:
            self.catalog[place.coordinates] = place
        else:
            raise AllThesePlacesException(f"this place exists already {str(place.coordinates)}")
        
        
class Agent:
    def __init__(self, 
                 identifier: str,
                 this_place: Place
                 ) -> None:
        self._identifier: str = identifier
        self._coordinates: Tuple[int, int, int] = this_place.coordinates
    
    @property
    def identifier(self):
        return self._identifier

    @property
    def coordinates(self):
        return self._coordinates
    
    @coordinates.setter
    def coordinates(self, value: Tuple[int, int, int]) -> None:
        assert sum(value) == 0 
        self._coordinates = value
