from linked_list_sentinel import SentinelLinkedList, Element

L = SentinelLinkedList()
L.insert(Element(3))
L.insert(Element(2))
L.insert(Element(1))
L.show()
print(L.search(2).key)
L.delete(L.search(2))
L.show()