from igraph import *

g2 = Graph.Tree(127,2)
summary(g2)

quick = g2.get_edgelist()[0:10]
print(quick)

