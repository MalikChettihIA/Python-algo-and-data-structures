def parent(i):
    return (i-1)//2
def left(i):
    return 2*i +1
def right(i):
    return 2*i +1

class Heap:
    
    def __init__(self, tab):
        self.lenght = len(tab)
        self.v = tab
        self.heapsize = 0
        self.nbMaxHeapify = 0
        
    def show(self):
        print("lenght = ", self.lenght)
        print("heapsize = ", self.heapsize)
        print("values = ", self.v)
        
    def max_heapify(self, i):
        print("max_heapify -> ", i)
        self.nbMaxHeapify +=1 
        l = left(i); r=right(i)
        
        if l < self.heapsize and self.v[l] > self.v[i]:
            largest = l
        else:
            largest = i
            
        if r < self.heapsize and self.v[r] > self.v[largest]:
            largest = r
            
        if largest != i:
            self.v[largest], self.v[i] = self.v[i], self.v[largest]
            self.max_heapify(largest)             
    
    def build_max_heap(self):
        self.heapsize =self.lenght
        for i in range((self.lenght-1)//2, -1, -1):
            self.max_heapify(i)
            
    def heap_sort(self):
        self.build_max_heap()
        for i in range(self.lenght-1, 0, -1):
            self.v[0], self.v[i] = self.v[i], self.v[0] 
            self.heapsize -= 1
            self.max_heapify(0)                   