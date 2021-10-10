import random
from heap import heap

def getVertexCover(adjList):

    nVertices = len(adjList)

    edgeCounts = []
    for i in range(len(adjList)):
        edgeCounts.append(len(adjList[i]))

    maxHeap = heap(edgeCounts)

    for i in range(nVertices):
        maxHeap.insert(i)

    visited = [False] * nVertices

    vertexCover = []
    while(maxHeap.isPopulated()):
        
        #for i in range(len(maxHeap.eIndices)):
        #    print(edgeCounts[maxHeap.eIndices[i]], end=", ")
        #print()
        #print(maxHeap.eIndices)

        index, value = maxHeap.pop()
        edgeCounts[index] = 0

        #print("index", index, "value", value)
        if (value == 0):
            break

        vertexCover.append(index)
        visited[index] = True

        for adj in adjList[index]:
            if not visited[adj]:
                #print(adj)
                edgeCounts[adj] -= 1
            
        maxHeap.fixAll()

    vertexCover.sort()
    return vertexCover

#print(getVertexCover([[1,2,4],[0,3,4],[0,3,5],[1,2],[0,1],[2]]))
#print(getVertexCover([[1, 2, 5], [0, 2, 4], [0, 1, 3, 5], [2, 5], [1, 5, 6], [0, 2, 3, 4, 6], [4, 5]]))
#print(getVertexCover([[1, 2, 5], [0, 2, 4], [0, 1, 3, 5], [2, 5], [1, 5, 6], [0, 2, 3, 4, 6], [4, 5]]))
