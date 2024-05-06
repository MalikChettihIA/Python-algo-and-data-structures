from binary_tree import BinaryTree, Node

BT = BinaryTree()
BT.root = Node(3)
BT.root.addChild(7, "left")
BT.root.addChild(9, "right")
BT.root.rightChild.addChild(2, "left")
#BT.root.explore()
BT.root.iterativeExplore()