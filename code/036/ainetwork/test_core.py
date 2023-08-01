from core import Link, Graph
from typing import Tuple

def test(g: Graph, red: int, blue: int) -> Tuple[int, int, bool]:
    return red, blue, g.test_link((red, blue))

def main():
    graph = Graph()
    
    graph.create_link(1, 2)
    graph.create_link(1, 3)    
    graph.create_link(1, 4)    
    graph.create_link(2, 5)        
    graph.create_link(2, 6)
    graph.create_link(3, 7)
    graph.create_link(3, 8)    
    graph.create_link(3, 9)    
    graph.create_link(4, 10)        
    graph.create_link(4, 11)
    graph.create_link(5, 0)        
    graph.create_link(6, 0)
    graph.create_link(7, 0)
    graph.create_link(8, 0)    
    graph.create_link(9, 0)    
    graph.create_link(10, 0)        
    graph.create_link(11, 0)
    
    print(str(test(graph, 1, 2)))
    print(str(test(graph, 1, 0)))
    
    for node in graph.nodes():
        links = graph.divergent_links(node)
        print(node)
        for a_link in links:
            print('  ', str(a_link))
    
    for node in graph.nodes():
        links = graph.convergent_links(node)
        print(node)
        for a_link in links:
            print('  ', str(a_link))
        

if __name__ == '__main__':
    main()

    
