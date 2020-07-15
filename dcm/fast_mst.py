# A Python program for Prims's MST for  
# adjacency list representation of graph 
  
import math
import numpy as np
from collections import defaultdict


# Converts from adjacency matrix to adjacency list 
def convert_matrix_to_list(matrix):
    adjList = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                newNode = [j, matrix[i][j]] 
                adjList[i].append(newNode)

                # newNode = [i, matrix[i][j]]
                # adjList[j].append(newNode)
    return adjList
  
  
class Heap(): 
    def __init__(self): 
        self.array = [] 
        self.size = 0
        self.pos = [] 
  
    def newMinHeapNode(self, v, dist): 
        minHeapNode = [v, dist] 
        return minHeapNode 
  
    # A utility function to swap two nodes of  
    # min heap. Needed for min heapify 
    def swapMinHeapNode(self, a, b): 
        t = self.array[a] 
        self.array[a] = self.array[b] 
        self.array[b] = t 
  
    # A standard function to heapify at given idx 
    # This function also updates position of nodes  
    # when they are swapped. Position is needed  
    # for decreaseKey() 
    def minHeapify(self, idx): 
        smallest = idx 
        left = 2 * idx + 1
        right = 2 * idx + 2
  
        if left < self.size and self.array[left][1] < self.array[smallest][1]: 
            smallest = left 
  
        if right < self.size and self.array[right][1] < self.array[smallest][1]: 
            smallest = right 
  
        # The nodes to be swapped in min heap  
        # if idx is not smallest 
        if smallest != idx: 
            # Swap positions 
            self.pos[ self.array[smallest][0] ] = idx 
            self.pos[ self.array[idx][0] ] = smallest 
  
            # Swap nodes 
            self.swapMinHeapNode(smallest, idx) 
  
            self.minHeapify(smallest) 
  
    # Standard function to extract minimum node from heap 
    def extractMin(self): 
        # Return NULL wif heap is empty 
        if self.isEmpty() == True: 
            return
  
        # Store the root node 
        root = self.array[0] 
  
        # Replace root node with last node 
        lastNode = self.array[self.size - 1] 
        self.array[0] = lastNode 
  
        # Update position of last node 
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
  
        # Reduce heap size and heapify root 
        self.size -= 1
        self.minHeapify(0) 
  
        return root 
  
    def isEmpty(self): 
        return True if self.size == 0 else False
  
    def decreaseKey(self, v, dist): 
        # Get the index of v in  heap array
        i = self.pos[v] 
  
        # Get the node and update its dist value 
        self.array[i][1] = dist 
  
        # Travel up while the complete tree is not  
        # hepified. This is a O(Logn) loop 
        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]:
            # Swap this node with its parent 
            self.pos[ self.array[i][0] ] = (i-1) // 2
            self.pos[ self.array[(i-1)//2][0]] = i 
            self.swapMinHeapNode(i, (i - 1) // 2) 
  
            # move to parent index 
            i = (i - 1) // 2; 

    # A utility function to check if a given vertex 
    # 'v' is in min heap or not 
    def isInMinHeap(self, v): 
        if self.pos[v] < self.size: 
            return True
        return False


class Graph(): 
    def __init__(self, adjacency_matrix): 
        self.V = adjacency_matrix.shape[0] 
        self._graph = convert_matrix_to_list(adjacency_matrix)

    def _build_edges(self, parent, n):
        edges = []
        for i in range(1, n): 
            edges.append([parent[i], i])
        return np.array(edges)

    # The main function that prints the Minimum  
    # Spanning Tree(MST) using the Prim's Algorithm.  
    # It is a O(ELogV) function 
    def PrimMST(self): 
        # Get the number of vertices in graph 
        V = self.V   
          
        # key values used to pick minimum weight edge in cut 
        key = []    
          
        # List to store contructed MST 
        parent = []  
  
        # minHeap represents set E 
        minHeap = Heap() 
  
        # Initialize min heap with all vertices. Key values of all 
        # vertices (except the 0th vertex) is is initially infinite 
        for v in range(V): 
            parent.append(-1) 
            key.append(math.inf) 
            minHeap.array.append(minHeap.newMinHeapNode(v, key[v])) 
            minHeap.pos.append(v) 
  
        # Make key value of 0th vertex as 0 so  
        # that it is extracted first 
        minHeap.pos[0] = 0
        key[0] = 0
        minHeap.decreaseKey(0, key[0]) 
  
        # Initially size of min heap is equal to V 
        minHeap.size = V
  
        # In the following loop, min heap contains all nodes 
        # not yet added in the MST. 
        while minHeap.isEmpty() == False: 
            # Extract the vertex with minimum distance value 
            newHeapNode = minHeap.extractMin() 
            u = newHeapNode[0] 
  
            # Traverse through all adjacent vertices of u  
            # (the extracted vertex) and update their  
            # distance values 
            for pCrawl in self._graph[u]:
                v = pCrawl[0] 
  
                # If shortest distance to v is not finalized  
                # yet, and distance to v through u is less than 
                # its previously calculated distance 
                if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]: 
                    key[v] = pCrawl[1] 
                    parent[v] = u 
  
                    # update distance value in min heap also 
                    minHeap.decreaseKey(v, key[v]) 
  
        return self._build_edges(parent, V)


def MST(adjacency_matrix):
    graph = Graph(adjacency_matrix)
    return graph.PrimMST()

# Debug
# if __name__ == "__main__":
#     a = np.array(
#           [[0, 9, 75, 2, 0, 10],
#           [9, 0, 95, 19, 42, 99],
#           [75, 95, 0, 51, 66, 12],
#           [2, 19, 51, 0, 31, 22],
#           [0, 42, 66, 31, 0, 89],
#           [10, 99, 12, 22, 89, 0]]
#         )

#     graph = Graph(a)
#     print("Adjacency List:") 
#     for i in graph._graph: 
#         print(i, end ="") 
#         for node in graph._graph[i]: 
#             print(" -> {}".format(node[0]), end ="") 
#         print()

#     print("="*20)
#     MST = graph.PrimMST()
#     print(MST)
