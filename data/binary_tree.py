class Node:
    
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        
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
            
        if self.rightChild != None:
            print("right = ", self.rightChild.key ,end=", ")
        else:
            print("right = ", "/" ,end=", ")  
        
        print(")")
            
    def addChild(self, key, direction):
        x = Node(key)
        x.parent = self
        
        if direction == 'left':
            if self.leftChild != None:
                raise Exception('Left child already exists !')
            else:
                self.leftChild = x
                
        if direction == 'right':
            if self.rightChild != None:
                raise Exception('Right child already exists !')
            else:
                self.rightChild = x
    
    def explore(self):
        self.show()
        if self.leftChild != None:
            self.leftChild.explore()
        if self.rightChild != None:
            self.rightChild.explore()
    
    # Utilisation d'une pile pour itérer
    def iterativeExplore(self):
        S = [self]
        while len(S) > 0:
            x = S.pop()
            x.show()
            if x.leftChild != None:
                S.append(x.leftChild)
            if x.rightChild != None:
                S.append(x.rightChild)
                
class BinaryTree:
    
    def __init__(self):
        self.root = None                
                    