import math
import numpy as np
from collections import defaultdict
 
# Converts from adjacency matrix to adjacency list 
def convert_matrix_to_list(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > 0:
                adjList[i].append(j)
    return adjList


def MST(G):
    """
    Find a Minimum Spanning Tree using Prim's Algorithm
        - G: an adjacency matrix representing a graph
    """

    tree = []

    INF = math.inf

    # Number of vertices in graph
    V = G.shape[-1]

    # Create a set S to track selected vertices
    # selected vertices will become true otherwise false
    S = np.zeros(V, dtype=bool)

    # Initialize number of edge to 0
    n_edges = 0

    # The number of edges in Minimum Spanning Tree will be
    # always less than (V - 1), where V is the number of vertices in the graph

    # Choose 0th vertex and make it true
    S[0] = True

    # For every selected vertex in the set S, find all adjacent vertices 
    # that are not included in the set S.
    # Choose an adjacent vertex that is nearest to one of selected vertices.
    while (n_edges < V - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if S[i]:
                for j in range(V):
                    if ((not S[j]) and G[i][j]):
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        S[y] = True
        tree.append([x, y])
        n_edges += 1
    return np.array(tree)


if __name__ == "__main__":
    a = np.array(
          [[0, 9, 75, 2, 0, 10],
          [9, 0, 95, 19, 42, 99],
          [75, 95, 0, 51, 66, 12],
          [2, 19, 51, 0, 31, 22],
          [0, 42, 66, 31, 0, 89],
          [10, 99, 12, 22, 89, 0]]
        )
    adjList = convert_matrix_to_list(a)
    print("Adjacency List:") 
    for i in adjList: 
        print(i, end ="") 
        for j in adjList[i]: 
            print(" -> {}".format(j), end ="") 
        print()

    print(MST(a))
