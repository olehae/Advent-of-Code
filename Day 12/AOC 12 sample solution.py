import numpy as np
import networkx as nx

H = np.array([[*x.strip()] for x in open("input12.txt")])

S = tuple(*np.argwhere(H == 'S'))  # get start coordinates
H[S] = 'a'  # start has elevation a
E = tuple(*np.argwhere(H == 'E'))  # get end coordinates
H[E] = 'z'  # end has elevation z

G = nx.grid_2d_graph(*H.shape, create_using=nx.DiGraph)  # create graph from 2d np array with edges to all 4 sides
# DiGraph: directed edges, no parallel edges

G.remove_edges_from([(a, b) for a, b in G.edges if ord(H[b]) > ord(H[a])+1])  # remove edges if height difference > 1

print(f"Shortest path length from S to E: {nx.shortest_path_length(G, source=S, target=E)}")

p = nx.shortest_path_length(G, target=E)  # shortest path length from every node to E
print(f"Shortest path length from any a to E: {min(p[a] for a in p if H[a] == 'a')}")
