import random

def partition(A, p, r):
    x = A[r]
    i = p -1
    for j in range(p, r):
        if A[j] <= x:
            i = i +1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def patition_randomized(A,p,r):
    i = random.randint(p,r)
    A[i],A[r]=A[r],A[i]                
    return partition(A,p,r)

'''
quick_sort(A)

The quick_sort function performs the iterative Quicksort algorithm. 
It operates by utilizing a stack to manage the subarrays that need to be sorted. 
The stack keeps track of subarray ranges through pairs of indices (p, r). 
The function initializes the stack and pushes the initial range of the entire array onto it. 
It then enters a loop where it repeatedly pops subarray ranges from the stack, applies 
the partition function to find the pivot’s position, and pushes subarray ranges onto the 
stack for further processing. This loop continues until the stack becomes empty, indicating 
that all subarrays have been sorted.
'''
def quick_sort(A):
    S = [(0, len(A)-1)]
    while len(S) > 0:
        p, r = S.pop()
        if p < r:
            q = patition_randomized(A,p,r)
            S.append([p, q-1])
            S.append([q+1, r])
            
            
            
            
