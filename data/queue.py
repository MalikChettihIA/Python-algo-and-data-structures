class Queue:
    
    def __init__(self, n):
        self.lenght =n
        self.Q = list(range(n))
        self.tail = 0               #queue
        self.head = 0               #tete
        
    def show(self):
        if self.empty():
            print("Queue is empty")
            return 
        else:
            print("Q = (", end= " ")
            if self.tail > self.head:
                for i in range(self.head,self.tail):
                    print(self.Q[i], end= " ")
            else:
                for i in range(self.head,self.lenght):
                    print(self.Q[i], end= " ")
                for i in range(self.tail):
                    print(self.Q[i], end= " ") 
        print(")")
   
    def empty(self):
        return self.tail == self.head
        
    def full(self):
        return (self.tail + 1) % self.lenght == self.head
    
    def enqueue(self, x):
        if self.full():
            raise Exception("Queue Overflow")
        else:
            self.Q[self.tail] = x
            if self.tail == self.lenght:
                self.tail = 1
            else:
                self.tail += 1    
        
    def dequeue(self):
        if self.empty():
            raise Exception("Queue Underflow")
        else:
            x = self.Q[self.head]
            if self.head == self.lenght:
                self.head = 1 
            else:
                self.head += 1
        return x                         