def binary_search(A, start, end, X):
    if start <= end:
        middle = (start + end)//2
        if A[middle] == X :
            return middle
        if X < A[middle]:
            return binary_search(A, start, middle-1, X)
        if X > A[middle] :
            return binary_search(A, middle+1, end, X)
    return -1 # number not found

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    index = binary_search(array, 0, 9, 10)
    print(index)
