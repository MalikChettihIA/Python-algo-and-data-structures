def counting_sort(A,k):
    B = list(A)
    C=[]
    for i in range(k+1):
        C.append(0)
    #print("C1 = ", C)    
    for i in range(len(A)):
        C[A[i]] += 1
    #print("C2 = ", C)    
    for i in range(1, k+1):
        C[i] += C[i-1]
    #print("C3 = ", C)    
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -=1
    return B        
           