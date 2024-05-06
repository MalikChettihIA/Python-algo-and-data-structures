class Element:
    
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None
        
    def show(self):
        print("E[", end="")
        
        if self.prev != None:
            print(self.prev.key, end=",") 
        else:
            print("/", end=",")
        
        print("",self.key, end=",")
        
        if self.next != None:
            print(self.next.key, end="") 
        else:
            print("/", end="")
            
        print("]", end="")
        
class LinkedList:
     
    def __init__(self):
        self.head = None

    def show(self):
        if self.empty():
            print("LikedList()")
        else:
            x = self.head
            print("LikedList(", end="")
            while x != None:
                x.show()
                x = x.next
            print(")")    
    
    def empty(self):
        return self.head == None
    
    def search(self, k):
        x = self.head
        while x != None and x.key != k:
            x = x.next
        return x
    
    def insert(self, x):
        if not isinstance(x, Element):
            raise Exception("Exception - x is not an Element")
        else:   
            x.prev = None
            x.next = self.head
            if self.head != None:
                self.head.prev = x
            self.head = x
            
    def delete(self, x):
        if not isinstance(x, Element):
            raise Exception("Exception - x is not an Element")
        
        if self.empty():
            raise Exception("Exception - List is empty")
        
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next    
        
        if x.next != None:
            x.next.prev = x.prev      
    
    def removeIfLess(self):
        x = self.head
        while x.next != None:
            y = x.next
            if y.key < x.key:
                if y.next == None:
                    x.next = None
                else:
                    x.next = y.next
                    y.next.prev = x
            else:
                x = y                                     
                