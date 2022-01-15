from igraph import *

g6 = Graph.Full(10)
only_odd_vertices = g6.vs.select(lambda vertex: vertex.index % 2 == 1)
print(only_odd_vertices())