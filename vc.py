
import json
import random

output = {}

threesholds = []

for line in open("threesholds.txt", "r"):
    threesholds.append(int(line.split(' ')[1]))

nPass = 0

total = 200
for i in range(1,total, 2):
    print(i)

    ### READ DATA
    directory = "graphs/"
    fileName = "vc-exact_" + str(i).zfill(3) + ".gr"
    file = open(directory + fileName, "r")

    firstLine = file.readline()
    nVertices = int(firstLine.split(' ')[2])
    nEdges = int(firstLine.split(' ')[3])

    ### BUILD GRAPH
    adjEdges = []
    edges = []
    covered = [False] * nEdges
    inVertexCover = [False] * nVertices

    for j in range(nVertices):
        adjEdges.append([])

    for line in file.readlines():
        
        arr = line.split(' ')

        adjEdges[int(arr[0])-1].append(len(edges))
        adjEdges[int(arr[1])-1].append(len(edges))

        edges.append([int(arr[0])-1, int(arr[1])-1])


    ### VC ALGO
    indexList = list(range(nEdges))
    random.shuffle(indexList)

    for j in indexList:

        if covered[j]:
            continue

        u = edges[j][0]
        v = edges[j][1]

        inVertexCover[u] = True
        inVertexCover[v] = True

        covered[j] = True

        for adj in adjEdges[u]:
            covered[adj] = True

        for adj in adjEdges[v]:
            covered[adj] = True

    vertexCover = []
    for j in range(0, nVertices):
        if inVertexCover[j]:
            vertexCover.append(j)

    nPass += len(vertexCover) < threesholds[int((i-1)/2)]
    print(int((i-1) / 2))
    
    output[fileName] = vertexCover
    print(len(vertexCover) < threesholds[int((i-1)/2)])
    print(len(vertexCover))

print("Passed: ", nPass, " / ", total)
with open('data.json', 'w') as outfile:
    json.dump(output, outfile)
            




