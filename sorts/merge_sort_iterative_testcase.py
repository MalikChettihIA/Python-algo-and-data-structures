import merge_sort_iterative
import random
import time 


random.seed(2024)
n = int(10)
A = [random.randrange(0,100) for i in range(n)]
t0 = time.time()
print("Before ", A)
merge_sort_iterative.merge_sort(A, 0, len(A)-1)
t1 = time.time()
print("Temps merge sort ", round(t1-t0, 2), " s")
print("After ", A)