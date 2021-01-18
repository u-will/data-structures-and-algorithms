from ..Graph import Graph

def depth_first(vertex):
    list_vertex = []
    def walk (root):
        if root in list_vertex:
            return
        list_vertex.append(root)

        neighbor= [Edge.vertex for Edge in GetNeighbors(root)]
        for vertex in neighbor:
            walk(vertex)
    walk(vertex)
    return list_vertex
