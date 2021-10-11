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

        index, value = maxHeap.pop()
        edgeCounts[index] = 0

        if (value == 0):
            continue

        vertexCover.append(index)
        visited[index] = True

        for adj in adjList[index]:
            if not visited[adj] and not edgeCounts[adj] == 0:
                edgeCounts[adj] -= 1
                maxHeap.fix(maxHeap.extToInt[adj])

    vertexCover.sort()
    return vertexCover
