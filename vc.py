import random

def getVertexCover(nEdges, nVertices, adjEdges, edges):

    # 1. Split into disconnected subgraphs
    # 2. Check each supgraph if is tree or bipartite
    # 3. Apply cheap vertex cover for tree and bipartite subgraphs
    # 4. Apply approximate vertex cover on rest of the graph

    print(checkIfBipartite(nEdges, nVertices, adjEdges, edges))
    min = nVertices
    minCover = []

    for i in range(10):
  
        indexList = list(range(nEdges))
        random.shuffle(indexList)

        covered = [False] * nEdges
        inVertexCover = [False] * nVertices

        for j in indexList:

            if covered[j]:
                continue

            u = edges[j][0]
            v = edges[j][1]

            inVertexCover[u] = True
            inVertexCover[v] = True

            for adj in adjEdges[u]:
                covered[adj] = True

            for adj in adjEdges[v]:
                covered[adj] = True


        vertexCover = []
        for j in range(0, nVertices):
            if inVertexCover[j]:
                # offset for output
                vertexCover.append(j+1)

        if len(vertexCover) < min:
            min = len(vertexCover)
            minCover = vertexCover


    return vertexCover

def splitIntoSubGraphs(nEdges, nVertices, adjEdges, edges):
    visited = [False] * nVertices

    stack = []
    for i in range(nVertices):
        if not visited[i]:
            stack.append(i)

        while(stack):
            v = stack.pop()

            stack.append(adjEdges[v])



def checkIfBipartite(nEdges, nVertices, adjEdges, edges):

    color = [-1] * nVertices

    for i in range(nEdges):
        c1 = color[edges[i][0]]
        c2 = color[edges[i][1]]

        if c1 == -1 and c2 == -1:
            color[edges[i][0]] = 0
            color[edges[i][1]] = 1
            continue

        if (c1 == 0 and c2 == -1) or (c1 == -1 and c2 == 1):
            color[edges[i][0]] = 0
            color[edges[i][1]] = 1

        if (c1 == 1 and c2 == -1) or (c1 == -1 and c2 == 0):
            color[edges[i][0]] = 1
            color[edges[i][1]] = 0

        if c1 == c2:
            return False

    return True


#print(getVertexCover(4, 4, [[0, 3],[0, 1],[1,2],[2,3]], [[0,1],[1,2],[2,3],[3,0]]))