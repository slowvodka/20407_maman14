import random


class QuickSort:
    def __init__(self, arr: list):
        self.arr = arr
        self.count = 0

    def setArr(self, arr):
        self.arr = arr

    def swap(self, nums, i, j):
        '''helper function to swap'''
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def partition(self, left, right, pindex):
        '''func that partition for quick sort'''

        # Pick `pindex` as a pivot from the list
        pivot = self.arr[pindex]

        # Move pivot to end
        self.swap(self.arr, pindex, right)

        pindex = left

        # if we find an element <= pivot, `pindex` is incremented. that element placed before pivot
        for i in range(left, right):
            if self.arr[i] <= pivot:
                self.count += 1
                self.swap(self.arr, i, pindex)
                pindex = pindex + 1

        # Move pivot to its place
        self.swap(self.arr, pindex, right)

        return pindex

    def quickSelect(self, left, right, k):
        ''' main func to select k-th smallest'''

        # If  one element, return element
        if left == right:
            self.count += 1
            return left, self.arr[left]

        # rnd select
        pindex = random.randint(left, right)

        pindex = self.partition(left, right, pindex)

        if k == pindex:
            self.count += 1
            return pindex, self.arr[k]

        # if `k` < pivot index
        elif k < pindex:
            self.count += 1
            return self.quickSelect(left, pindex - 1, k)

        # if `k` > pivot index
        else:
            return self.quickSelect(pindex + 1, right, k)

    def quickSort(self, left, right):
        ''' Function to perform quicksort'''
        if left < right:
            self.count += 1
            pi = self.partition(left, right, (left + right) // 2)
            self.quickSort(left, pi - 1)
            self.quickSort(pi + 1, right)

    def compareCounter(self):
        return self.count
