from core import AllThesePlaces, Place, Agent
import random

class Engine:
    def __init__(self):
        self._all_these_places = AllThesePlaces()
        self._all_these_places.add_place(Place(0,0))
        self._all_these_places.add_place(Place(1,0))
        self._all_these_places.add_place(Place(0,1))
        self._all_these_places.add_place(Place(-1,0))
        self._all_these_places.add_place(Place(0,-1))
        self._all_these_places.add_place(Place(-1,1))    
        self._all_these_places.add_place(Place(1,-1))
        self._all_these_places.add_place(Place(2,0))
        self._all_these_places.add_place(Place(1,1))
        self._all_these_places.add_place(Place(0,2))
        self._all_these_places.add_place(Place(-1,2))
        self._all_these_places.add_place(Place(-2,2))    
        self._all_these_places.add_place(Place(-2,1))
        self._all_these_places.add_place(Place(-2,0))
        self._all_these_places.add_place(Place(-1,-1))
        self._all_these_places.add_place(Place(0,-2))
        self._all_these_places.add_place(Place(1,-2))
        self._all_these_places.add_place(Place(2,-2))    
        self._all_these_places.add_place(Place(2,-1))
        agents = []
        for location, place in self._all_these_places.catalog.items():
            for p in range(random.randint(1, 9)):
                identifier = f'bota-{p:d}{random.randint(1, 1000):>03d}'
                agents.append(Agent(identifier, place))
        self._agents = agents
    
if __name__ == '__main__':
    start()
    
