from core import AllThesePlaces, Place

def main():
    top = 2
    all_these_places = AllThesePlaces('Simula')
    all_these_places.add_place(Place(0,0))
    all_these_places.add_place(Place(1,0))
    all_these_places.add_place(Place(0,1))
    all_these_places.add_place(Place(-1,0))
    all_these_places.add_place(Place(0,-1))
    all_these_places.add_place(Place(-1,1))    
    all_these_places.add_place(Place(1,-1))
    
    all_these_places.add_place(Place(2,0))
    all_these_places.add_place(Place(1,1))
    all_these_places.add_place(Place(0,2))
    all_these_places.add_place(Place(-1,2))
    all_these_places.add_place(Place(-2,2))    
    all_these_places.add_place(Place(-2,1))

    all_these_places.add_place(Place(-2,0))
    all_these_places.add_place(Place(-1,-1))
    all_these_places.add_place(Place(0,-2))
    all_these_places.add_place(Place(1,-2))
    all_these_places.add_place(Place(2,-2))    
    all_these_places.add_place(Place(2,-1))

    
    for location, place in all_these_places.catalog.items():
        print(str(location), place.radii)
    
if __name__ == '__main__':
    main()
    
