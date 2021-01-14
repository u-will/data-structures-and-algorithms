from ..Graph import Graph
from .test_get_edge import direct_flights

def test_flights():
    graph = Graph()
    metroville = graph.AddNode("Metroville")
    pandora = graph.AddNode("Pandora")
    arendelle = graph.AddNode("Arendelle")

    graph.AddEdge(pandora, arendelle, 150)
    graph.AddEdge(arendelle, pandora, 150)

    graph.AddEdge(pandora, metroville, 82)
    graph.AddEdge(metroville, pandora, 82)

    graph.AddEdge(metroville, arendelle, 99)
    graph.AddEdge(arendelle, metroville, 99)

    assert direct_flights(graph, ["Metroville","Pandora"]) == (True,82)
    assert direct_flights(graph, ["Metroville","arendelle"]) == (True,99)
    assert direct_flights(graph, ["arendelle","Pandora"]) == (True,150)
