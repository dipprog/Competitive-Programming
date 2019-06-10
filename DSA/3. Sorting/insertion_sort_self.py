def insertion_sort(A):
    for curr in range(len(A)):
        prev = curr
        while (prev >= 0):
            if (A[prev] > A[curr]):
                A[curr], A[prev] = A[prev], A[curr]
                curr = prev
            prev = prev -1

if __name__ == '__main__':
    size = int(input())
    A = list(map(int, (input().split(" "))))
    insertion_sort(A)
    print(A)
