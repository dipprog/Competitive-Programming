# Heap Size
heap_size = 10
# Function to get right child
def get_right_child(A,index):
    if (2*index+1) < len(A) and index >= 1:
        return (2*index+1)
    return -1
# Function to get left child
def get_left_child(A,index):
    if (2*index) < len(A) and index >= 1:
        return (2*index)
    return -1
# Function to get Parent
def get_parent(A,index):
    if (index > 1) and (index < len(A)):
        return index//2
    return -1
# Defining Max_heapify Function
def max_heapify(A,index):
    left_child_index = get_left_child(A,index)
    right_child_index = get_right_child(A,index)
    # Finding the largest among left, right and index
    largest = index
    if (left_child_index <= heap_size) and (left_child_index > 0):
        if A[left_child_index] > A[largest]:
            largest = left_child_index
    if (right_child_index <= heap_size) and (right_child_index > 0):
        if A[right_child_index] > A[largest]:
            largest = right_child_index
    # Largest is not the node, node is not a heap
    if(largest != index):
        A[index], A[largest] = A[largest], A[index]
        max_heapify(A,largest)
# Building Max_heapify
def build_max_heap(A):
    for i in range(heap_size//2, 0, -1):
        max_heapify(A,i)
# Utility Function
if __name__ == '__main__':
    # tree is starting from index 1 not 0
    A = [0, 4, 5, 12, 34, 67, 66, 15, 22, 10, 3]
    build_max_heap(A)
    print(A[1:])
