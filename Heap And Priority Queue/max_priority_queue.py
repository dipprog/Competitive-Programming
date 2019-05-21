heap_size = 0
tree_array_size = 20
INF = 100000
# Get right child
def get_right_child(A, index):
    if ((2*index + 1) < len(A)) and (index >=1):
        return (2*index + 1)
    return -1
# Get left child
def get_left_child(A, index):
    if ((2*index) < len(A)) and (index >=1):
        return (2*index)
    return -1
# Get parent
def get_parent(A, index):
    if (index < len(A)) and (index > 1):
        return index//2
    return -1
# MAX-HEAPIFY function
def max_heapify(A, index):
    left_child_index = get_left_child(A, index)
    right_child_index = get_right_child(A, index)
    # Find largest among them
    largest = index
    if (left_child_index > 0) and (left_child_index <= heap_size):
        if A[left_child_index] > A[largest]:
            largest = left_child_index
    if (right_child_index > 0) and (right_child_index <= heap_size):
        if A[right_child_index] > A[largest]:
            largest = right_child_index
    # if node is not the largest and node is not a heap
    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        max_heapify(A, largest)
# Build MAX-HEAP function
def build_max_heap(A):
    for i in range(heap_size//2, 0, -1):
        max_heapify(A,i)
# ***************************Max-Prioriry Queue Operation**************************
# Get Maximum
def maximum(A):
    return A[1]
# Extract Maximum
def extract_maximum(A):
    global heap_size
    maxE = A[1]
    A[1] = A[heap_size]
    heap_size = heap_size -1
    max_heapify(A, 1)
    return maxE
# Increase Key
def increase_key(A, i, key):
    A[i] = key
    while (i > 1) and (A[get_parent(A,i)] < A[i]):
        A[i], A[get_parent(A,i)] = A[get_parent(A,i)], A[i]
        i = get_parent(A, i)
# Decrease Key
def decrease_key(A, i, key):
    A[i] = key
    max_heapify(A,i)
# Insert Key
def insert(A, key):
    global heap_size
    heap_size = heap_size+1
    A[heap_size] = -1*INF
    increase_key(A, heap_size, key)
# Driving function
if __name__ == '__main__':
    A = [None]*tree_array_size
    insert(A, 20)
    insert(A, 15)
    insert(A, 8)
    insert(A, 10)
    insert(A, 5)
    insert(A, 7)
    insert(A, 6)
    insert(A, 2)
    insert(A, 9)
    insert(A, 1)

    print(A[1:heap_size+1])

    increase_key(A, 5, 22)
    print(A[1:heap_size+1])

    print(maximum(A))
    print(extract_maximum(A))

    print(A[1:heap_size+1])

    print(extract_maximum(A))
    print(extract_maximum(A))
    print(extract_maximum(A))
    print(extract_maximum(A))
    print(extract_maximum(A))
    print(extract_maximum(A))
    print(extract_maximum(A))
    print(extract_maximum(A))
    print(extract_maximum(A))
