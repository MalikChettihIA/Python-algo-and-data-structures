# Inerstion Sort Python Implementation.
# Worst case is in Θ(n*2)
# Best case is in Θ(n)

def insert_sort(A, n):
    for i in range(1, len(A)):
        key = A[i]
        j = i -1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key