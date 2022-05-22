import sys


# defining a class min_heap for the heap data structure

class MinHeap:

    def __init__(self, sizelimit):
        self.sizelimit = sizelimit
        self.cur_size = 0
        self.heap = [0] * (self.sizelimit + 1)
        self.heap[0] = sys.maxsize * -1
        self.root = 1
        self.count = 0

    def Swap(self, node1, node2):
        '''helper function to swap the two given nodes of the heap
    # this function will be needed for heapify and insertion to swap nodes not in order'''
        self.heap[node1], self.heap[node2] = self.heap[node2], self.heap[node1]

    def minHeapify(self, i):
        '''THE minHeapify FUNCTION'''

        # If the node is a not a leaf node and is greater than any of its child
        if not ((self.cur_size // 2) <= i <= self.cur_size):
            if self.heap[i] > self.heap[2 * i] or self.heap[i] > self.heap[(2 * i) + 1]:
                self.count += 2
                if self.heap[2 * i] < self.heap[(2 * i) + 1]:
                    self.count += 1
                    # Swap the node with the left child and then call the minHeapify function on it
                    self.Swap(i, 2 * i)
                    self.minHeapify(2 * i)

                else:
                    # Swap the node with right child and then call the minHeapify function on it
                    self.Swap(i, (2 * i) + 1)
                    self.minHeapify((2 * i) + 1)


    def Insert(self, element):
        '''THE INSERT FUNCTION'''
        if self.cur_size >= self.sizelimit:
            return
        self.cur_size += 1
        self.heap[self.cur_size] = element
        current = self.cur_size
        while self.heap[current] < self.heap[current // 2]:
            self.Swap(current, current // 2)
            current = current // 2

    def heapPop(self):
        '''THE HEAPPOP FUNCTION'''
        last = self.heap[self.root]
        self.heap[self.root] = self.heap[self.cur_size]
        self.cur_size -= 1
        self.minHeapify(self.root)
        return last

    def buildHeap(self):
        '''THE BUILD_HEAP FUNCTION'''
        for i in range(self.cur_size // 2, 0, -1):
            self.minHeapify(i)

    def Print(self):
        '''helper function to print the heap'''
        for i in range(1, (self.cur_size // 2) + 1):
            print("Parent Node is " + str(self.heap[i]) + " Left Child is " + str(
                self.heap[2 * i]) + " Right Child is " + str(self.heap[2 * i + 1]))

    def compareCounter(self):
        return self.count
