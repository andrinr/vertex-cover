

for i in range(1,5):

    fileName = "graphs/vc-exact_" + str(i).zfill(3) + ".gr"
    file = open(fileName, "r")

    firstLine = file.readline()
    nVertices = int(firstLine.split(' ')[2])
    nEdges = int(firstLine.split(' ')[3])


    adjVertices = []
    edges = []
    visited = []

    for i in range(nVertices):
        adjVertices.append([])
        visited.append(False)

    for line in file.readlines():
        
        arr = line.split(' ')

        adjVertices[int(arr[0])-1].append(int(arr[1])-1)
        adjVertices[int(arr[1])-1].append(int(arr[0])-1)

        edges.append([ int(arr[0])-1, int(arr[1])-1])

    for i in range(nEdges):

        u = edges[i][0]
        v = edges[i][1]

        if not visited[u]:

            for adj in adjVertices[u]:

                if not visited[adj]:

                    visited[u] = True
                    visited[v] = True

                    break

    
    for i in range(nVertices):



