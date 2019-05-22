def selection_sort(A):
    index =0
    for pos in range(len(A)):
        min_value = min(A[index:])
        index_min = A.index(min_value)
        A[index], A[index_min] = A[index_min], A[index]
        index=index+1
if __name__ == '__main__':
    A = [7, 8, 3, 4, 56, 34, 11]
    print(A)
    selection_sort(A)
    print(A)
