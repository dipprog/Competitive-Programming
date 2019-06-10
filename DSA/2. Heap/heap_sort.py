import heap as hp
def heap_sort(A):
    heap_size = len(A)-1
    hp.build_max_heap(A)
    for i in range(heap_size,1,-1):
        A[1], A[i] = A[i], A[1]
        heap_size = heap_size -1
        hp.max_heapify(A,1,heap_size)

if __name__ == '__main__':
    Arr = [0,6,5,10,4,3,1]
    print(Arr[1:])
    heap_sort(Arr)
    print(Arr[1:])
