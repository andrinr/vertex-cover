
import json
import vc

output = {}

threesholds = []

for line in open("threesholds.txt", "r"):
    threesholds.append(int(line.split(' ')[1]))

nPass = 0

total = 200
for i in range(1,total, 2):

    ### READ DATA
    directory = "graphs/"
    fileName = "vc-exact_" + str(i).zfill(3) + ".gr"
    file = open(directory + fileName, "r")
    print(fileName)

    firstLine = file.readline()
    nVertices = int(firstLine.split(' ')[2])
    nEdges = int(firstLine.split(' ')[3])

    ### BUILD GRAPH
    adjList = []
    edges = []

    for j in range(nVertices):
        adjList.append([])

    for line in file.readlines():
        
        arr = line.split(' ')

        u = int(arr[0])-1
        v = int(arr[1])-1

        adjList[u].append(v)
        adjList[v].append(u)

        edges.append([u,v])

    vertexCover = vc.getVertexCover(adjList)

    ### TEST
    nPass += len(vertexCover) <= threesholds[int((i-1)/2)]
    covered = [False] * nVertices

    for j in range(len(vertexCover)):
        covered[vertexCover[j]] = True

    for u, v in edges:
        if not covered[u] and not covered[v]:
            print("Mistake detected")
            break

    ### OUTPUT
    for j in range(len(vertexCover)):
        vertexCover[j] += 1

    output[fileName] = vertexCover 

    print(len(vertexCover), "/", threesholds[int((i-1)/2)], "/", nVertices)

print("Passed: ", nPass, " / ", total/2)
with open('data.json', 'w') as outfile:
    json.dump(output, outfile)
            




