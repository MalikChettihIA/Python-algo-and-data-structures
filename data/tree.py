class Node:
    
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.leftChild = None
        self.rightSibling = None
        
    def show(self):
        print("Node (", end=" ")

        if self.key != None:
            print("key = ", self.key ,end=", ")
        else:
            print("parent = ", "/" ,end=", ")
                    
        if self.parent != None:
            print("parent = ", self.parent.key ,end=", ")
        else:
            print("parent = ", "/" ,end=", ")
            
        if self.leftChild != None:
            print("left = ", self.leftChild.key ,end=", ")
        else:
            print("left = ", "/" ,end=", ")
            
        if self.rightSibling != None:
            print("rightSibling = ", self.rightSibling.key ,end=", ")
        else:
            print("rightSibling = ", "/" ,end=", ")  
        
        print(")")    
        
    def addLeftChild(self, key):
        x = Node(key)
        x.parent = self
        x.rightSibling = self.leftChild
        self.leftChild = x  
        
    def explore(self):
        self.show()
        x = self.leftChild
        while x != None:
            x.explore()
            x = x.rightSibling
    
    # Utilisation d'une file pour itérer        
    def iterativeExplore(self):
        S = [self]
        while len(S) > 0:
            x = S.pop()
            x.show()
            x = x.leftChild
            while x != None:
                S = [x]+S
                x = x.rightSibling
    
    def count(self):
        nbNode = 0
        S = [self]
        while len(S) > 0:
            x = S.pop()
            nbNode+=1
            x = x.leftChild
            while x != None:
                S = [x]+S
                x = x.rightSibling
        return nbNode

    def countLeaves(self):
        nbLeaves = 0
        S = [self]
        while len(S) > 0:
            x = S.pop()
            if x.leftChild == None:
                nbLeaves+=1
            x = x.leftChild
            while x != None:
                S = [x]+S
                x = x.rightSibling
        return nbLeaves    
    
class Tree:
    
    def __init__(self):
        self.root = None                      