def partition(A, start, end):
    pivot = A[end]
    i = start-1
    for j in range(start, end):
        if A[j] <= pivot:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[end] = A[end], A[i+1]
    return i+1
def quick_sort(A, start, end):
    if start < end:
        q = partition(A, start, end)
        quick_sort(A, start, q-1)
        quick_sort(A, q+1, end)
if __name__ == '__main__':
    A =  [4, 8, 1, 3, 10, 9, 2, 11, 5, 6]
    print(A)
    quick_sort(A, 0, 9)
    print(A)
