from ..Graph import graph
def direct_flights(graph, location):


    # we will use the zip function.  here how the zip function works:
    # if we have [A,B,C,D] and [a,b,c],
    # zip([A,B,C,D], [a,b,c]) => [(A,a),(B,b), (C,c)]
    #  we only concider the smallest list of elements
    destination_name = location[1]
    origin_name = location[0]
    cost = 0
    for origin_name, destination_name in zip(location, location[1:])
        nodes = graph.GetNodes()
        origin_node = None

        for candidate_node in nodes:
            if candisdate_node.value == origin_name:
                origin_node = candidate_node
                break
        if not origin_node:
            return False, 0

        edges = graph.GetNeighbors(origin_node)
        destination_node = None

        for edges in edges:
            if edges.vertex.value == destination_name:
                cost += edge.weight
                destination_node = edge.vertex
                break
         if not destination_node:
             return False, 0

    return True,cost
