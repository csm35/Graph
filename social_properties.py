from igraph import *

g5 = Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
summary(g5)


g5.vs["name"] = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
g5.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
g5.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
g5.es["is_formal"] = [False, False, True, True, True, False, True, False, False]

print(g5.degree())
print(g5.degree([2,3,4]))

print(g5.edge_betweenness())

print(g5.vs.select(_degree=g5.maxdegree())["name"])



