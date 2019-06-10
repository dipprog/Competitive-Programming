def optimized_bubble_sort(A):
    for i in range(len(A)):
        swapped = False
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True
        if not swapped:
            break;

A = [20,15,10,3,4,5]
print(A)
optimized_bubble_sort(A)
print(A)
