# Graphs can have all kinds of shapes, made up of trees and linkedlists
# E <= V^2, E = Edges, V = Vertex
# cycles can form, directed graphs have directions
# matrix (more commom)
# adjacency matrix
# adjacency list (more common)

# Matrix
# 0 0 1
# 1 0 0
# 1 0 0
# R x C
# arr[1][0] = 1
# cells (free places, 0's) could represent nodes

# Adjacency Matrix
# adjMatrix[v1][v2] = 1 -> an edge exists from v1 to v2
# row and columns represent edges, usually boolean as cell value, 0 or 1

# Adjacency List
# use an array
# list out neighbors for each node
# basically whatever the node is pointing to
# for undirected, then whatever it is connected too

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
