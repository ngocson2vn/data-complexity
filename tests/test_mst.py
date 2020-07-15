import numpy as np
import dcm

# Create a adjacency matrix to represent graph
G = np.array(
      [[0, 9, 75, 2, 0, 10],
      [9, 0, 95, 19, 42, 99],
      [75, 95, 0, 51, 66, 12],
      [2, 19, 51, 0, 31, 22],
      [0, 42, 66, 31, 0, 89],
      [10, 99, 12, 22, 89, 0]]
    )
print("Adjacency Matrix:\n{}\n".format(G))

MST = dcm.MST(G)
print("Minimum Spanning Tree:\n{}".format(MST))