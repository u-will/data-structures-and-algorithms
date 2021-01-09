from graph import Graph, Vertex, Edge

def test_addNode():
    graph = Graph()
    vertex = graph.AddNode("hello")
    assert isinstance(vertex, Vertex)

def test_check_value_addednode():
    graph = Graph()
    actuel = graph.AddNode("spam").value
    expected = "spam"
    assert actuel == expected

def test_AddEdge():
    graph = Graph()
    start = graph.AddNode('start')
    end = graph.AddNode('end')
    graph.AddEdge(start,end)

def test_AddEdge_weight():
    graph = Graph()
    start = graph.AddNode('start')
    end = graph.AddNode('end')
    weight = 10
    graph.AddEdge (start, end, weight)


def test_AddEdge_interloper_start():
    graph = Graph()
    start = Vertex('start')
    end = graph.AddNode('end')
    # with pytest.raises(KeyError):
    #     graph.AddEdge(start, end)
def test_GetNodes():
    graph = Graph()
    banana = graph.AddNode('banana')
    apple = graph.AddNode('apple')
    expected = 2
    actual = len(graph.GetNodes())
    assert actual == expected

def test_size_empty():
    graph = Graph()

    expected = 0
    actual = graph.Size()
    assert actual == expected

def test_size_1():
    graph = Graph()
    graph.AddNode('spam')
    expected = 1
    actual = graph.Size()
    assert actual == expected

def test_size_2():
    graph = Graph()
    graph.AddNode('spam')
    graph.AddNode('bacon')
    expected = 2
    actual  = graph.Size()
    assert actual == expected

def test_GetNeighbors_none():
     graph = Graph()
     banana = graph.AddNode('banana')
     neighbors = graph.GetNeighbors(banana)
     assert len(neighbors) == 0

def test_GetNeighbors_return_edges():
    graph = Graph()
    banana = graph.AddNode('banana')
    apple = graph.AddNode('apple')
    graph.AddEdge(apple, banana)
    neighbors = graph.GetNeighbors(apple)

    assert len(neighbors) == 1
    neighbor = neighbors[0]
    assert isinstance(neighbor, Edge)

    assert neighbor.vertex.value == 'banana'

def test_neighbors_with_default_weight():
    graph = Graph()
    banana = graph.AddNode('banana')
    apple = graph.AddNode('apple')
    graph.AddEdge(apple, banana)
    neighbor = graph.GetNeighbors(apple)
    actual = neighbor[0].weight
    expected = 0
    assert actual == expected

def test_neighbors_with_custom_weight():
    graph = Graph()
    banana = graph.AddNode('banana')
    apple = graph.AddNode('apple')
    graph.AddEdge(apple, banana,44)
    neighbor = graph.GetNeighbors(apple)
    actual = neighbor[0].weight
    expected = 44
    assert actual == expected
