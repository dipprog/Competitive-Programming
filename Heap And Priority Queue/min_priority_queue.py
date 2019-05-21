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
# MIN-HEAPIFY function
def min_heapify(A, index):
    left_child_index = get_left_child(A, index)
    right_child_index = get_right_child(A, index)
    # Find smallest among them
    smallest = index
    if (left_child_index > 0) and (left_child_index <= heap_size):
        if A[left_child_index] < A[smallest]:
            smallest = left_child_index
    if (right_child_index > 0) and (right_child_index <= heap_size):
        if A[right_child_index] < A[smallest]:
            smallest = right_child_index
    # if node is not the smallest and node is not a heap
    if smallest != index:
        A[index], A[smallest] = A[smallest], A[index]
        min_heapify(A, smallest)
# Build MIN-HEAP function
def build_min_heap(A):
    for i in range(heap_size//2, 0, -1):
        min_heapify(A,i)
# ***************************Min-Prioriry Queue Operation**************************
# Get minimum
def minimum(A):
    return A[1]
# Extract minimum
def extract_minimum(A):
    global heap_size
    minE = A[1]
    A[1] = A[heap_size]
    heap_size = heap_size -1
    min_heapify(A, 1)
    return minE
# Decrease Key
def decrease_key(A, i, key):
    A[i] = key
    while (i > 1) and (A[get_parent(A,i)] > A[i]):
        A[i], A[get_parent(A,i)] = A[get_parent(A,i)], A[i]
        i = get_parent(A, i)
# Increase Key
def increase_key(A, i, key):
    A[i] = key
    min_heapify(A,i)
# Insert Key
def insert(A, key):
    global heap_size
    heap_size = heap_size+1
    A[heap_size] = INF
    decrease_key(A, heap_size, key)
# Driving function
if __name__ == '__main__':
    # tree is starting from index 1 and not 0
    A = [0, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
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

    decrease_key(A, 1, 13)
    print(A[1:heap_size+1])

    print(minimum(A))
    print(extract_minimum(A))

    print(A[1:heap_size+1])

    print(extract_minimum(A))
    print(extract_minimum(A))
    print(extract_minimum(A))
    print(extract_minimum(A))
    print(extract_minimum(A))
    print(extract_minimum(A))
    print(extract_minimum(A))
    print(extract_minimum(A))
    print(extract_minimum(A))
