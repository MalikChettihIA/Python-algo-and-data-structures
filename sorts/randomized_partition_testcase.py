import randomized_partition

A=[5,8,2,5,7,3,1]
i = 1
print("i=", i, " ordre stat =", randomized_partition.randomized_select(A,0,len(A)-1,i))
i = 7
print("i=", i, " ordre stat =", randomized_partition.randomized_select(A,0,len(A)-1,i))
i = (len(A)+1)//2
print("i=", i, " ordre stat =", randomized_partition.randomized_select(A,0,len(A)-1,i))