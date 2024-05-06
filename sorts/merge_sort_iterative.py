import math

def merge_sort(A, p, r):
    if p < r:
        S = [(p,r)]
        print("S = [(p,r)] ", S)
        while len(S) > 0:
            p, r = S.pop()
            print("p, r = S.pop() ", S)
            q = (p+r)//2
            merge(A, p, q, r)
            
            S.append([p, q])
            print("S.append([p, q]) ", S)
            S.append([q+1, r])
            print("S.append([q+1, r]) ", S)
            

        

def merge(A, p, q, r):
    L = A[p:q+1]; L.append(math.inf); i=0
    R = A[q+1:r+1]; R.append(math.inf); j=0
    for k in range(p,r):
        if L[i] <= R[j]:
            A[k] = L[i]; i += 1
        else:
            A[k] = R[j]; j += 1
                      