from typing import Tuple, Dict, Generator

Link = Tuple[int, int]

class Graph:
    def __init__(self) -> None:
        self._links: Dict[Link, bool] = {}

    @property
    def links(self) -> Dict[Link, bool]:
        return self._links
    
    def nodes(self):
        _nodes: Dict[int, bool] = {}
        for key, value in self.links.items():
            _nodes[key[0]] = True
            _nodes[key[1]] = True
        for key in sorted(_nodes.keys()):
            yield key            

    def create_link(self, red: int, blue: int) -> Link:
        this_link = (red, blue)
        self.links[this_link] = True
        return this_link
    
    def test_link(self, this_link: Link) -> bool:
        return self.links.get(this_link, False)

    def divergent_links(self, red: int) -> Generator[Link, None, None]:
        return (key for key in self.links.keys() if key[0] == red)
    
    def convergent_links(self, blue: int) -> Generator[Link, None, None]:
        return (key for key in self.links.keys() if key[1] == blue)
