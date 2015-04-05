from binary_heap_min_heap import BinHeap

def heap_sort(a_list):
    min_heap = BinHeap()
    min_heap.build_heap(a_list)
    return min_heap.heap_list[1:]


print heap_sort([9, 6, 5, 2, 3])
