from igraph import *

g5 = Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
summary(g5)


g5.vs["name"] = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
g5.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
g5.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
g5.es["is_formal"] = [False, False, True, True, True, False, True, False, False]

print(g5.vs[1])

print(g5.es[5])

print(g5.es[5].source)
print(g5.es[5].target)

g5.vs[1]["name"] = "Chickahominy"
print(g5.vs[1].attributes())

g5["date"] = "01-57-2347"
print(g5["date"])













