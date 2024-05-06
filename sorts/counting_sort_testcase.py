import random
import counting_sort
import time

# Expected Case
A = [2,5,3,0,2,3,0,3]
k = 5
print("Counting Sort (Expected Case) - Before A = ", A)
print("Counting Sort (Expected Case) - Before k = ", k)
t0 = time.time()
B = counting_sort.counting_sort(A,k)
t1 = time.time()
print("Counting Sort (Expected Case) - After B = ", B)
print("Counting Sort (Expected Case) - After time = ", round(t1-t0, 2), " s")

#Best Case
n = int(1e2)
A = []
k = 0
for i in range(n):
    A.append(random.randint(0, n//10))
    if k < A[i]:
        k = A[i]
print("Counting Sort (Best Case) - Before A = ", A)
print("Counting Sort (Best Case) - Before k = ", k)
t0 = time.time()
B = counting_sort.counting_sort(A,k)
t1 = time.time()
print("Counting Sort (Best Case) - After B = ", B)
print("Counting Sort (Best Case) - After time = ", round(t1-t0, 2), " s")       

# Worst case
A=[0,int(1e7), 1]
k=max(A)

print("Counting Sort (Worst Case) - Before A = ", A)
print("Counting Sort (Worst Case) - Before k = ", k)
t0 = time.time()
B = counting_sort.counting_sort(A,k)
t1 = time.time()
print("Counting Sort (Worst Case) - After B = ", B)
print("Counting Sort (Worst Case) - After time = ", round(t1-t0, 2), " s")  