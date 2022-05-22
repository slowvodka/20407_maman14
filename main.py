
import pandas as pd
from heap_sort import *
from rand_select import *


MIN_NUM = 0
MAX_NUM = 999


def getN():
    '''get N from user'''
    n = -1
    while n<1:
        print('please enter number of elements you want from array:')
        n = int(input())
        if n > 0:
            return n
        else:
            print(f'n should be positive integer')

def getK(n):
    '''get K from user based on previous N'''
    k = n+1
    while k > n or k <1:
        print('please enter number of min elements you want to get:')
        k = int(input())
        if k > 0 and k<=n:
            return k
        else:
            print(f'{k} should be between 1 to {n}')

def getRandomIntArray(n: int):
    '''func to generate a random array in len {n}'''
    print(f'random array in of {n} elements is generated')

    random_list = []
    for i in range(n):
        random_list.append(random.randint(MIN_NUM, MAX_NUM))
    return random_list


def getIntArrayFromUser(n: int):
    ''' func gets an array in len {n} from user'''
    print(f'please enter {n} elements one by one:')

    return [int(input()) for i in range(n)]


def getArray(n, opt = -1):
    ''' func to get array'''
    print('please specify how to enter the array: enter a number of the option')
    print('1. random array')
    print('2. manual input array')
    while opt != 1 and opt != 2:
        opt = int(input())
        if opt != 1 and opt != 2:
            print('please choose between 1 or 2')
    if opt == 1:
        return getRandomIntArray(n)
    if opt == 2:
        return getIntArrayFromUser(n)


def buildHeap(arr: list):
    ''' func to build min heap from array'''
    min_heap = MinHeap(len(arr) + 1)
    for i in arr:
        min_heap.Insert(i)
    min_heap.buildHeap()
    return min_heap


def kMinFromHeap(heap: MinHeap, k: int):
    ''' func to extract k min elements from heap
    func also prints number of comparissons it took
    '''
    min_k = []
    for i in range(k):
        min_k.append(heap.heapPop())
    print(f"min k elements: {min_k}")
    print(f'comparisons counter: {heap.compareCounter()}')
    return heap.compareCounter()

def kMinFromQuickSort(arr: list, k: int):
    qso = QuickSort(arr)
    qso.quickSelect(0, len(arr) - 1, k)
    qso.setArr(arr[:k])
    qso.quickSort(0, k - 1)
    print(f"min k elements: {qso.arr}")
    print(f'comparisons counter: {qso.compareCounter()}')
    return qso.compareCounter()

def small_check():
    si = {100: {}, 200: {}, 500: {}, 1000: {}}
    hi = {100: {}, 200: {}, 500: {}, 1000: {}}

    for n in [100, 200, 500, 1000]:
        for k in [8, 50, 99]:
            hi[n][k] = 0
            si[n][k] = 0

    rng = 1000
    for i in range(rng):
        for n in [100, 200, 500, 1000]:
            for k in [8, 50, 99]:
                arr = getArray(n, opt=1)
                h = kMinFromHeap(buildHeap(arr), k)
                s = kMinFromQuickSort(arr, k)
                hi[n][k] += h
                si[n][k] += s

    for n in [100, 200, 500, 1000]:
        for k in [8, 50, 99]:
            hi[n][k] /= rng
            si[n][k] /= rng

    print('heap')
    print(pd.DataFrame(hi))
    print("*" * 10)
    print('quick')
    print(pd.DataFrame(si))


def main(checks = 0):

    if checks == 0:
        #for both
        n = getN()
        k = getK(n)

        arr = getArray(n, opt=1)
        print(f"N is {n}")
        print(f"K is {k}")
        print(f"arr is {arr}\n")

        # heap
        print('\nusing heap')
        kMinFromHeap(buildHeap(arr), k)

        # select
        print('\nusing select')
        kMinFromQuickSort(arr, k)

    if checks == 1:
        small_check()


main(1)


