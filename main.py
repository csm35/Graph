from igraph import *

g1 = Graph()

g1.add_vertices(3)
g1.add_edges([(0,1),(1,2)])
g1.add_edges([(2,0)])
g1.add_vertices(3)
g1.add_edges([(2,3),(3,4),(4,5),(5,3)])
print(g1)

cut = g1.get_eid(2,3)# names one at a time by index
print(cut)

g1.delete_edges(3)# deletes one at a time by index
print(g1)

summary(g1) #prints just the no of vertices and edges








