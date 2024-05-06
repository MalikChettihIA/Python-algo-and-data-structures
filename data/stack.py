class Stack:
    
    def __init__(self, n):
        self.length = n              # Besoin pour tester l'overflow.
        self.S = list(range(n))   
        self.top = -1                # 0 en pseudo code.
        
        
    def show(self):
        print("S = ( ", end="")
        for i in range (self.top+1):
            print(self.S[i], end = " ")
        print(")")
        
    def empty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def push(self, x):
        if self.top == self.length-1:
             raise Exception('Stack Overflow')
        else:
          self.top +=1 
          self.S[self.top] = x
    
    def pop(self):
        if self.empty():
             raise Exception('Stack Underflow')
        else:
            self.top -=1
            return self.S[self.top+1]                   