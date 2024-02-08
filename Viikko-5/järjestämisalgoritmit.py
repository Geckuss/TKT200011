import time
import random
from typing import List

# Lisäysjärjestäminen
def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

# Lomitusjärjestäminen
def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Luo satunnainen lista
n = 10**5
arr = list(range(1, n+1))
random.shuffle(arr)

# Mittaa lisäysjärjestämisen suoritusaika
start = time.time()
insertion_sort(arr.copy())
end = time.time()
print(f"Insertion sort time: {end - start} seconds")

# Mittaa lomitusjärjestämisen suoritusaika
start = time.time()
merge_sort(arr.copy())
end = time.time()
print(f"Merge sort time: {end - start} seconds")

# Mittaa Pythonin sort-metodin suoritusaika
start = time.time()
arr.sort()
end = time.time()
print(f"Python sort time: {end - start} seconds")