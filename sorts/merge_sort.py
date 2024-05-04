import math

## Merge sort 
def merge_sort(A, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    L = A[p:q+1]; L.append(math.inf); i=0
    R = A[q+1:r+1]; R.append(math.inf); j=0
    
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]; i += 1
        else:
            A[k] = R[j]; j += 1    
            
         
        
    