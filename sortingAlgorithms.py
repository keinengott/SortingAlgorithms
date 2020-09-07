# Author: Robert Kaufman
#  Purpose: To analyze the efficiency of different sorting algorithms

import time
import matplotlib.pyplot as plt
import random
import sys

sys.setrecursionlimit(10**9)

def selectionSort(A):
    for i in range(len(A)): 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
                      
        A[i], A[min_idx] = A[min_idx], A[i] 

def insertionSort(A):
    for i in range(1, len(A)): 
        key = A[i] 
        j = i-1
        while j >=0 and key < A[j] : 
                A[j+1] = A[j] 
                j -= 1
        A[j+1] = key

def bubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]

def bubbleSortSwapCount(A):
    n = len(A)
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]
                swaps += 1
        if swaps == 0:
            return

def quickSort(A, minIndex, maxIndex):
    if minIndex >= maxIndex:
        return

    p = partition(A, minIndex, maxIndex)
    quickSort(A, minIndex, p-1)
    quickSort(A, p+1, maxIndex)

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              A[k] = left[i]
              i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k]=right[j]
            j += 1
            k += 1


def generateArrays(x, y, z, n):
    x.clear()
    y.clear()
    z.clear()
    for i in range(n):
        if i % 10 == 0:
            x.append(random.randint(1,10000))
        else:
            x.append(i)
        y.append(random.randint(1,10000))
        z.append(i)

n=1000
x = []     #Every 10th random
y = []     #All random
z = []      #Sorted list

timedResults = []  # A list of tuples containing the times it takes to sort each array

go1 = False
go2 = False
go3 = False
go4 = False
go5 = False
go6 = False

q=[1,10,100]
for i in range(3):
    generateArrays(x, y, z, n*q[i])
    t = time.time()
    insertionSort(x)
    u = time.time()
    timedResults.append(u-t)

if (go1):
    # Selection Sorting
    generateArrays(x, y, z, n)
    s = time.time()
    selectionSort(x)
    t = time.time()
    selectionSort(y)
    u = time.time()
    selectionSort(z)
    v = time.time()
    timedResults.append((t-s,u-t,v-u))
    print(timedResults)
if (go2):
    # Insertion Sorting
    generateArrays(x, y, z, n)
    s = time.time()
    insertionSort(x)
    t = time.time()
    insertionSort(y)
    u = time.time()
    insertionSort(z)
    v = time.time()
    timedResults.append((t-s,u-t,v-u))
    print(timedResults)
if (go3):
    # Bubble Sorting
    generateArrays(x, y, z, n)
    s = time.time()
    bubbleSort(x)
    t = time.time()
    bubbleSort(y)
    u = time.time()
    bubbleSort(z)
    v = time.time()
    timedResults.append((t-s,u-t,v-u))
    print(timedResults)
if (go4):
    # Bubble Sorting with Swaps
    generateArrays(x, y, z, n)
    s = time.time()
    bubbleSortSwapCount(x)
    t = time.time()
    bubbleSortSwapCount(y)
    u = time.time()
    bubbleSortSwapCount(z)
    v = time.time()
    timedResults.append((t-s,u-t,v-u))
    print(timedResults)
if (go5):
    # Quick Sorting
    generateArrays(x, y, z, n)
    s = time.time()
    quickSort(x, 0, (len(x)-1))
    t = time.time()
    quickSort(y, 0, (len(y)-1))
    u = time.time()
    #quickSort(z, 0, (len(z)-1))    
    v = time.time()
    timedResults.append((t-s,u-t,v-u))
    print(timedResults)
if (go6):
    # Merge Sorting
    generateArrays(x, y, z, n)
    s = time.time()
    mergeSort(x)
    t = time.time()
    mergeSort(y)
    u = time.time()
    mergeSort(z)
    v = time.time()
    timedResults.append((t-s,u-t,v-u))
    print(timedResults)
print(timedResults)

#xAxis = ["SS-Case1", "SS-Case2", "SS-Case3","IS-Case1", "IS-Case2", "IS-Case3","BS-Case1", "BS-Case2", "BS-Case3"
#         ,"BSS-Case1", "BSS-Case2", "BSS-Case3","MS-Case1", "MS-Case2", "MS-Case3"]
#xAxis = ["SS-Case1", "SS-Case2", "SS-Case3","IS-Case1", "IS-Case2", "IS-Case3","BS-Case1", "BS-Case2", "BS-Case3"
#         ,"BSS-Case1", "BSS-Case2", "BSS-Case3","QS-Case1", "QS-Case2", "QS-Case3","MS-Case1", "MS-Case2", "MS-Case3"]
xAxis=["1000","10000","100000"]
yAxis = [timedResults[0],timedResults[1],timedResults[2]]
count = 0
#for i in range(6):
#    for j in range(3):
#        count+=1
#        yAxis.append(timedResults[i][j])
plt.bar(xAxis,yAxis)
plt.xlabel("N")
plt.ylabel("Time")
plt.show()
