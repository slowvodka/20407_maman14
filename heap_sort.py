import sys


# defining a class min_heap for the heap data structure

class MinHeap:

    def __init__(self, sizelimit):
        self.sizelimit = sizelimit
        self.cur_size = 0
        self.Heap = [0] * (self.sizelimit + 1)
        self.Heap[0] = sys.maxsize * -1
        self.root = 1
        self.count = 0

        # helper function to swap the two given nodes of the heap
    # this function will be needed for heapify and insertion to swap nodes not in order
    def Swap(self, node1, node2):
        self.Heap[node1], self.Heap[node2] = self.Heap[node2], self.Heap[node1]

    # THE minHeapify FUNCTION
    def minHeapify(self, i):

        # If the node is a not a leaf node and is greater than any of its child
        if not ((self.cur_size // 2) <= i <= self.cur_size):
            if self.Heap[i] > self.Heap[2 * i] or self.Heap[i] > self.Heap[(2 * i) + 1]:
                self.count+=2
                if self.Heap[2 * i] < self.Heap[(2 * i) + 1]:
                    self.count += 1
                    # Swap the node with the left child and then call the minHeapify function on it
                    self.Swap(i, 2 * i)
                    self.minHeapify(2 * i)

                else:
                    # Swap the node with right child and then call the minHeapify function on it
                    self.Swap(i, (2 * i) + 1)
                    self.minHeapify((2 * i) + 1)

    # THE INSERT FUNCTION
    def Insert(self, element):
        if self.cur_size >= self.sizelimit:
            return
        self.cur_size += 1
        self.Heap[self.cur_size] = element
        current = self.cur_size
        while self.Heap[current] < self.Heap[current // 2]:
            self.Swap(current, current // 2)
            current = current // 2

    # THE HEAPPOP FUNCTION
    def heapPop(self):
        last = self.Heap[self.root]
        self.Heap[self.root] = self.Heap[self.cur_size]
        self.cur_size -= 1
        self.minHeapify(self.root)
        return last

    # THE BUILD_HEAP FUNCTION
    def buildHeap(self):
        for i in range(self.cur_size // 2, 0, -1):
            self.minHeapify(i)

    # helper function to print the heap
    def Print(self):
        for i in range(1, (self.cur_size // 2) + 1):
            print("Parent Node is " + str(self.Heap[i]) + " Left Child is " + str(
                self.Heap[2 * i]) + " Right Child is " + str(self.Heap[2 * i + 1]))

    def compareCounter(self):
        return self.count


