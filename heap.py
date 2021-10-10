import sys

# max heap
class heap:
    # reference to external dataArray
    def __init__(self, dataArray):
        self.eData = dataArray
        self.eIndices = []

    # Get maximum value, in this case at index 0
    def getMax(self):
        return self.values[0]

    def insert(self, index):
        self.eIndices.append(index)
        self.bubbleUp(len(self.eIndices)-1)

    def delete(self, index):
        if (len(self.eIndices) == 1):
            self.eIndices.pop()
            return

        self.eIndices[index] = self.eIndices.pop()

    def fix(self, index):
        self.bubbleDown(index)
        self.bubbleUp(index)

    def fixAll(self):
        for i in range(len(self.eIndices)):
            self.fix(i)
        
    def pop(self):

        tmpIndex = self.eIndices[0]
        self.delete(0)

        return tmpIndex, self.eData[tmpIndex]

    def isPopulated(self):
        return len(self.eIndices) > 0

    def bubbleUp(self, index):
        if index == 0:
            return

        parentIndex = int(index / 2)

        if (self.eData[self.eIndices[parentIndex]] < self.eData[self.eIndices[index]]):
            self.swap(index, parentIndex)
            self.bubbleUp(parentIndex)

    # O(log n), make sure tree conditions are met
    def bubbleDown(self, index):
        n = len(self.eIndices)
        leftIndex = index * 2 + 1
        rightIndex = index * 2 + 2

        # Check weather index has left child
        if (leftIndex < n):
            childIndex = leftIndex
            # When right child is bigger than left child, go with right child
            if rightIndex < n and self.eData[self.eIndices[leftIndex]] < self.eData[self.eIndices[rightIndex]]:
                childIndex = rightIndex

            # When bigger of the two children is bigger than current, then swap
            if (self.eData[self.eIndices[childIndex]] > self.eData[self.eIndices[index]]):
                self.swap(index, childIndex)
                # And continue bubbling down
                self.bubbleDown(childIndex)
                
    # Swap helper function
    def swap(self, a, b):
        tmpIndex  = self.eIndices[b]
        self.eIndices[b] = self.eIndices[a]
        self.eIndices[a] = tmpIndex

