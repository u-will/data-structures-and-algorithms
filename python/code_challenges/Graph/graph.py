class Graph:
    def __init__(self):
        #Called an Adjacency List but it's really a Dictionary here
        self._adjacency_list={}
    def AddNode(self, value):
        vertex= Vertex(value)
        self._adjacency_list[vertex]=[]
        return vertex

    def AddEdge(self,start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list:
            raise KeyError(start_vertex+'not in the graph')
        if end_vertex not in self._adjacency_list:
            raise KeyError(end_vertex+"not in the graph")
        edge = Edge(end_vertex, weight)
        Adjacencies = self._adjacency_list[start_vertex] # which at the begining is an empty list []
        Adjacencies.append(edge)

    def GetNodes(self):
        return self._adjacency_list.keys()

    #  often this method it's  call get_edges
    def GetNeighbors(self,vertex):
        return self._adjacency_list[vertex]

    def Size(self):
        return len(self._adjacency_list)

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self,vertex, weight):
        self.vertex = vertex
        self.weight = weight
