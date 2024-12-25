"""
=====================
Minimum Spanning Tree
=====================

A minimum spanning tree (MST) is a subset of edges in a weighted, 
connected graph that connects all vertices together with the 
minimum possible total edge weight. The `minimum_spanning_tree`
function is used to compare the original graph with its MST.

"""


import networkx as nx
import matplotlib.pyplot as plt








# Shortest Path Dijkstra Algorithm
>>> G=nx.path_graph(5)
>>> print(nx.shortest_path(G,source=0,target=4))

>>> p=nx.shortest_path(G,source=0)# target not specified
>>> p[3]# shortest path from source=0 to target=3

>>> p=nx.shortest_path(G,target=4)# source not specified
>>> p[1]# shortest path from source=1 to target=4

>>> p=nx.shortest_path(G)# source, target not specified
>>> p[2][4 ]# shortest path from source=2 to target=4

# All pairs Short Path (APSP)

>>> G=nx.path_graph(5)
>>> print(path[0][4]) 
>>> length=dict(nx.all_pairs_shortest_path_length(G))
>>> G = nx.path_graph(5)

>>> for node in [0, 1, 2, 3, 4]:
... print(f"1 - {node}: {length[1][node]}")

>>> length[3][2]

# Single Source Shortest Path (SSSP)
G = nx.path_graph(5)
path = nx.single_source_shortest_path(G, 0)
path[4]
G = nx.path_graph(5)
length = nx.single_source_shortest_path_length(G, 0)
length[4]
 
for node in length:... print(f"{node}: {length[node]}")
 
length, path = nx.single_source_dijkstra(G, 0)
length[4]4>>> for node in [0, 1, 2, 3, 4]:... print(f"{node}: {length[node]}")
path[4]
length, path = nx.single_source_dijkstra(G, 0, 1)

path[0, 1]
G = nx.path_graph(5)

path = nx.single_source_dijkstra_path(G, 0)
path[4]  


# Random Walk
G=nx.star_graph(3)
random_path=nx.generate_random_paths(G,2)

G=nx.star_graph(3)
index_map={}
random_path=nx.generate_random_paths(G,3,index_map=index_map)
paths_containing_node_0=[random_path[path_idx]for path_idx in index_map.get(0,[])]


# MST
# Create a graph
G = nx.Graph()
G.add_edges_from(
    [
        (0, 1, {"weight": 4}),
        (0, 7, {"weight": 8}),
        (1, 7, {"weight": 11}),
        (1, 2, {"weight": 8}),
        (2, 8, {"weight": 2}),
        (2, 5, {"weight": 4}),
        (2, 3, {"weight": 7}),
        (3, 4, {"weight": 9}),
        (3, 5, {"weight": 14}),
        (4, 5, {"weight": 10}),
        (5, 6, {"weight": 2}),
        (6, 8, {"weight": 6}),
        (7, 8, {"weight": 7}),
    ]
)

# Find the minimum spanning tree
T = nx.minimum_spanning_tree(G)

# Visualize the graph and the minimum spanning tree
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=500)
nx.draw_networkx_edges(G, pos, edge_color="grey")
nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")
nx.draw_networkx_edge_labels(
    G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}
)
nx.draw_networkx_edges(T, pos, edge_color="green", width=2)
plt.axis("off")
plt.show()
