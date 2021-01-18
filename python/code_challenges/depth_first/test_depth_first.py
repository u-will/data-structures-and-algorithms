from depth_first import depth_first
from ..Graph import Graph

def test_depth_first():
    graph = Graph()

    A = graph.AddNode('A')
    B = graph.AddNode('B')
    C = graph.AddNode('C')
    D = graph.AddNode('D')
    E = graph.AddNode('E')
    F = graph.AddNode('F')
    G = graph.AddNode('G')
    H = graph.AddNode('H')
    graph.AddEdge(A,B)
    graph.AddEdge(A,D)
    graph.AddEdge(B,A)
    graph.AddEdge(D,A)
    graph.AddEdge(D,B)
    graph.AddEdge(B,D)
    graph.AddEdge(B,C)
    graph.AddEdge(C,B)
    graph.AddEdge(C,G)
    graph.AddEdge(G,C)
    graph.AddEdge(D,E)
    graph.AddEdge(E,D)
    graph.AddEdge(D,H)
    graph.AddEdge(H,D)
    graph.AddEdge(D,F)
    graph.AddEdge(F,D)
    graph.AddEdge(H, F)
    graph.AddEdge(F, H)
    actual = depth_first(A)
    expected = [A, B, C, G, D, E, H, F]
    assert actual == expected
