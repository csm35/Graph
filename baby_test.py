from igraph import *
import random

g = Graph(directed=True)                 #builds a 3:3 graph manually
g.add_vertices(3)
g.add_edges([(0, 1), (1, 0), (1, 2)])
g.vs["name"] = [600, 601, 602]
g.vs["vsize"] = 100
g.vs["vendo"] = [1, 3, 3]
g.vs["damage"] = 0
g.vs["fire"] = False
g.vs["load"] = 0

g.es["eweight"] = [1, 3, 2]
g.es["elent"] = [4, 1, 3]
g.es["epulpos"] = [3, 1, 2]

size_graph = 5                          #variables that help organize a bigger graph
pulmult = 10
tot_edges = 3
tot_vertices = 3
next_vindex = 3
next_eindex = 3
next_vname = 603
vsize = 100
vendo_list = range(1,4)
init_in_edges = 2
init_out_edges = 2
max_in_edges = 3
max_out_edges = 3
elent_list = range(1,5)
eweight_list = range(1,4)
epulpos_list = range(0,5)
list_vindexes = range(0,next_vindex)
list_eindexes = range(0,next_eindex)
list_vnames = range(600,next_vname)

while tot_vertices < size_graph:                        #builds a graph of size_graph

    g.add_vertices(1)                                   #adds a vertex w/ no edges
    g.vs[next_vindex]["name"] = next_vname
    g.vs[next_vindex]["vsize"] = vsize
    g.vs[next_vindex]["vendo"] = 2
    g.vs[next_vindex]["damage"] = 0
    g.vs[next_vindex]["fire"] = False
    g.vs[next_vindex]["load"] = 0

    new_out_edges = 0
    target = next_vindex - 1
    while new_out_edges < init_out_edges:
        g.add_edges([(next_vindex, target)])         #adds outgoing edges to the new vertex
        g.es[next_eindex]["eweight"] = 1
        g.es[next_eindex]["elent"] = 3
        g.es[next_eindex]["epulpos"] = 2
        next_eindex += 1
        tot_edges += 1
        target -= 1
        new_out_edges += 1

    new_in_edges = 0
    source = next_vindex - 2
    while new_in_edges < init_in_edges:
        g.add_edges([(source, next_vindex)])     #adds incoming edges to the new vertex
        g.es[next_eindex]["eweight"] = 2
        g.es[next_eindex]["elent"] = 3
        g.es[next_eindex]["epulpos"] = 3
        next_eindex += 1
        tot_edges += 1
        source -= 1
        new_in_edges += 1

    list_eindexes = range(0,next_eindex)           #updates the elists

    next_vname += 1                                #increments the vstuff
    tot_vertices += 1
    next_vindex += 1

    list_vnames = range(600,next_vname)            #updates the vlists
    list_vindexes = range(0,next_vindex)

layout = g.layout('circle')                   #displays the graph in Preview
visual_style = {}
visual_style["vertex_size"] = 40
visual_style["vertex_color"] = ["pink"]
visual_style["vertex_shape"] = ["circle"]
visual_style["vertex_label"] = g.vs["name"]
visual_style["edge_label"] = None       # g.es["elabel"]
visual_style["edge_curved"] = [-0.2]
visual_style["edge_width"] = g.es["eweight"]
visual_style["layout"] = layout
visual_style["bbox"] = (400, 400)
visual_style["margin"] = 70
Layout.rotate(layout,30)

#plot(g, **visual_style)

# for edge_descrip in g.es[0:]:                #prints all the attributes of everything
#      print(edge_descrip)
# #
# for vert_descrip in g.vs[0:]:
#      print(vert_descrip)
#
# for vindex_list in list_vindexes:
#     print(vindex_list)

def list_my_edges():                #prints the graph edges by vertex
    source_target = 0
    while source_target < size_graph:
        inedges = g.es.select(_target=source_target)
        outedges = g.es.select(_source=source_target)
        print(source_target)
        for all_in in inedges:
            print("incoming")
            print(all_in)
        for all_out in outedges:
            print("outgoing")
            print(all_out)
        source_target += 1
list_my_edges()

                                    # begins the dream cycle function here
command = ""
while True:
    command = input("enter 's' to run or 'q' to quit> ").lower()
    if command == "s":
        vert_selector = 0
        while vert_selector < size_graph:
            vert_load = g.vs[vert_selector]["load"]
            vendo_loader = g.vs[vert_selector]["vendo"]
            print(vert_selector)
            print(vendo_loader)
            print(vert_load)
            vert_load += vendo_loader
            print(vert_load)
            edge_selector = g.es.select(_target=vert_selector)
            for each_edge in edge_selector[0:]:
                print(each_edge)
                print(each_edge["eweight"])
                print(each_edge["epulpos"])
                if each_edge["epulpos"] >= 1:
                    each_edge["epulpos"] -= 1
                    print("hiya")
                else:
                    vert_load += each_edge["eweight"]*pulmult
                    print("bingo")
                print(each_edge["epulpos"])
            print("...")
            vert_selector += 1

    elif command == "q":
        break
    else:
        print("wrong command dude")
















