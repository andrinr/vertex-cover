import sys
import math

# max heap
# values are stored in external array
# if value in external array has changed its internal index can be found with heap.extToInt
# and heap conditions can be restored with heap.fix(heap.extToInt(index))
class heap:
    # reference to external dataArray
    def __init__(self, dataArray):
        self.extData = dataArray
        self.intToExt = []
        self.extToInt = []

    # Get maximum value, in this case at index 0
    def getMax(self):
        return self.values[0]

    def insert(self, index):
        self.intToExt.append(index)
        self.extToInt.append(index)
        self.bubbleUp(len(self.intToExt)-1)

    def delete(self, index):
        if (len(self.intToExt) == 1):
            self.intToExt.pop()
            return

        # Put last element to index
        self.swap(len(self.intToExt)-1, index)
        # Delete last element
        self.intToExt.pop()

        self.fix(index)

    def fix(self, index):
        self.bubbleDown(index)
        self.bubbleUp(index)
        
    def pop(self):

        tmpIndex = self.intToExt[0]
        self.delete(0)

        return tmpIndex, self.extData[tmpIndex]

    def isPopulated(self):
        return len(self.intToExt) > 0

    def bubbleUp(self, index):
        #print(self.eIndices)
        if index == 0:
            return

        parentIndex = math.floor((index - 1) / 2)
        #print(parentIndex)

        if (self.extData[self.intToExt[parentIndex]] < self.extData[self.intToExt[index]]):
            self.swap(index, parentIndex)
            self.bubbleUp(parentIndex)

    # O(log n), make sure tree conditions are met
    def bubbleDown(self, index):
        n = len(self.intToExt)
        leftIndex = index * 2 + 1
        rightIndex = index * 2 + 2

        # Check weather index has left child
        if (leftIndex < n):
            childIndex = leftIndex
            # When right child is bigger than left child, go with right child
            if rightIndex < n and self.extData[self.intToExt[leftIndex]] < self.extData[self.intToExt[rightIndex]]:
                childIndex = rightIndex

            # When bigger of the two children is bigger than current, then swap
            if (self.extData[self.intToExt[childIndex]] > self.extData[self.intToExt[index]]):
                self.swap(index, childIndex)
                # And continue bubbling down
                self.bubbleDown(childIndex)
                
    # Swap helper function
    def swap(self, a, b):
        tmpIndex = self.intToExt[b]
        self.intToExt[b] = self.intToExt[a]
        self.intToExt[a] = tmpIndex

        self.extToInt[self.intToExt[a]] = a
        self.extToInt[self.intToExt[b]] = b