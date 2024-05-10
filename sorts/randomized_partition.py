import random

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def randomized_patition(A,p,r):
    i = random.randint(p,r)
    A[i],A[r]=A[r],A[i]                
    return partition(A,p,r)

def randomized_select(A,p,r, i):
    if p == r:
        return A[p]
    q = randomized_patition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    if i < k:
        return randomized_select(A,p,q-1, i)
    else:
        return randomized_select(A,q+1,r, i-k)