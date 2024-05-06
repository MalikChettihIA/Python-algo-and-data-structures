class Element:
    
    def __init__(self, key):
        self.key = key
        self.prev = self
        self.next = self
        
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
        
class SentinelLinkedList:
     
    def __init__(self):
        self.nil = Element("Sentinel")

    def show(self):
        if self.empty():
            print("LikedList()")
        else:
            x = self.nil.next
            print("LikedList(", end="")
            while x != self.nil:
                x.show()
                x = x.next
            print(")")    
    
    def empty(self):
        return (self.nil.next == self.nil) and (self.nil.prev == self.nil)
    
    def search(self, k):
        x = self.nil.next
        while x != self.nil and x.key != k:
            x = x.next
        return x
    
    def insert(self, x):
        if not isinstance(x, Element):
            raise Exception("Exception - x is not an Element")
        else:   
            x.prev              = self.nil
            x.next              = self.nil.next
            self.nil.next.prev  = x
            self.nil.next       = x
            
    def delete(self, x):
        if not isinstance(x, Element):
            raise Exception("Exception - x is not an Element")
        
        if self.empty():
            raise Exception("Exception - List is empty")
        
        x.prev.next = x.next
        x.next.prev = x.prev   

    def removeIfLess(self):
        x = self.nil.next
        while x!=self.nil and x.next != self.nil:
            y = x.next
            if y.key < x.key:
                x.next = y.next
                y.next.prev = x
            else:
                x = y    
    def removeIfLess2(self):
        x = self.nil.next
        while x != self.nil:
            while x != self.nil and x.next != self.nil and x.next.key < x.key:
                x.next = x.next.next
                x.next.prev = x
                x = x.next
            x = x.next                            
                                
                