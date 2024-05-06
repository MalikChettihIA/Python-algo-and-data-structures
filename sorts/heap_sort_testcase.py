import heap_sort

A = [5, 9, 2, 7, 12, 5, 3, 4, 8, 3, 10, 9]
H = heap_sort.Heap(A)
H.build_max_heap()
H.show()
print('nbMaxHeapify -> ',H.nbMaxHeapify)