

for i in range(1,5):

    fileName = "graphs/vc-exact_" + str(i).zfill(3) + ".gr"
    file = open(fileName, "r")

    nVertices = -1
    nEdges = -1

    firstLine = True
    for line in file.readlines():
        
        arr = line.split(' ')

        if (firstLine):
            firstLine = False
            nVertices = arr[2]
            nEdges = arr[3]

    print(nEdges)
    print(nVertices)
