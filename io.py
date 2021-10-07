
import json
import random
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
    adjEdges = []
    edges = []

    for j in range(nVertices):
        adjEdges.append([])

    for line in file.readlines():
        
        arr = line.split(' ')

        u = int(arr[0])-1
        v = int(arr[1])-1

        adjEdges[u].append(len(edges))
        adjEdges[v].append(len(edges))

        edges.append([u,v])


    vertexCover = vc.getVertexCover(nEdges, nVertices, adjEdges, edges)

    nPass += len(vertexCover) < threesholds[int((i-1)/2)]
    
    output[fileName] = vertexCover 

    print(len(vertexCover), "/",threesholds[int((i-1)/2)], "/", nVertices)

print("Passed: ", nPass, " / ", total)
with open('data.json', 'w') as outfile:
    json.dump(output, outfile)
            




