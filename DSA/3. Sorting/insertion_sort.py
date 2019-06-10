def insertion_sort(A):
    for i in range(len(A)):
        j=i
        while (j > 0) and (A[j-1] > A[j]):
            A[j-1], A[j] = A[j], A[j-1]
            j = j-1

if __name__ == '__main__':
    ar = [4, 8, 1, 3, 10, 9, 2, 11, 5, 6]
    insertion_sort(ar)
    print(ar)
