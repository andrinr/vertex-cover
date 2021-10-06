

for i in range(1,5):

    fileName = "graphs/vc-exact_" + str(i).zfill(3) + ".gr"
    file = open(fileName, "r")

    firstLine = file.readline()
    nVertices = int(firstLine.split(' ')[2])
    nEdges = int(firstLine.split(' ')[3])


    adjVertices = []
    for i in range(nVertices):
        adjVertices.append([])

    for line in file.readlines():
        
        arr = line.split(' ')

        adjVertices[int(arr[0])-1].append(int(arr[1])-1)
        adjVertices[int(arr[1])-1].append(int(arr[0])-1)

    print(adjVertices)



