
import json
import random

output = {}

for i in range(1,201):
    print(i)

    directory = "graphs/"
    fileName = "vc-exact_" + str(i).zfill(3) + ".gr"
    file = open(directory + fileName, "r")

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

    indexList = list(range(nVertices))
    random.shuffle(indexList)

    for i in indexList:

        if not visited[i]:

            visited[i] = True

            for adj in adjVertices[i]:
                visited[adj] = True


    visitedList = []
    for i in range(nVertices):
        if visited[i]:
            visitedList.append(i)
    
    output[fileName] = visitedList

with open('data.json', 'w') as outfile:
    json.dump(output, outfile)
            




