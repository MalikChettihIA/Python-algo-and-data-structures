from linked_list import LinkedList, Element

L = LinkedList()
L.insert(Element(3))
L.insert(Element(2))
L.insert(Element(1))
L.show()
print(L.search(2).key)
L.delete(L.search(2))
L.show()