# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

fl = search.GPSProblem('F', 'L'
                       , search.romania)

dt = search.GPSProblem('D', 'T'
                       , search.romania)

az = search.GPSProblem('A', 'Z'
                       , search.romania)

bu = search.GPSProblem('B', 'U'
                       , search.romania)

print("Busqueda en anchura:")
print(search.breadth_first_graph_search(ab).path())
print(search.breadth_first_graph_search(fl).path())
print(search.breadth_first_graph_search(dt).path())
print(search.breadth_first_graph_search(az).path())
print(search.breadth_first_graph_search(bu).path())
print("\nBusqueda en profundidad:")
print(search.depth_first_graph_search(ab).path())
print(search.depth_first_graph_search(fl).path())
print(search.depth_first_graph_search(dt).path())
print(search.depth_first_graph_search(az).path())
print(search.depth_first_graph_search(bu).path())
print("\nBusqueda en ramificacion y acotacion:")
print(search.search_ramification(ab).path())
print(search.search_ramification(fl).path())
print(search.search_ramification(dt).path())
print(search.search_ramification(az).path())
print(search.search_ramification(bu).path())
print("\nBusqueda en ramificacion con subestimacion:")
print(search.search_ramification_understimated(ab).path())
print(search.search_ramification_understimated(fl).path())
print(search.search_ramification_understimated(dt).path())
print(search.search_ramification_understimated(az).path())
print(search.search_ramification_understimated(bu).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
