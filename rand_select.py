from random import randrange


class RandSort:
    def __init__(self, arr):
        self.arr = arr
        self.count = 0

    def partition(self, arr, pivot_index=0):
        i = 0
        if pivot_index != 0: arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
        for j in range(len(arr) - 1):
            if arr[j + 1] < arr[0]:
                arr[j + 1], arr[i + 1] = arr[i + 1], arr[j + 1]
                i += 1
        arr[0], arr[i] = arr[i], arr[0]
        return arr, i

    def RSelect(self, arr, k):
        if len(arr) == 1:
            return arr[0]
        else:
            xpart = self.partition(arr, randrange(len(arr)))
            arr = xpart[0]  # partitioned array
            j = xpart[1]  # pivot index
            if j == k:
                self.count += 1
                return arr[j]
            elif j > k:
                self.count += 1
                return self.RSelect(arr[:j], k)

            else:
                self.count += 1
                k = k - j - 1
                return self.RSelect(arr[(j + 1):], k)
