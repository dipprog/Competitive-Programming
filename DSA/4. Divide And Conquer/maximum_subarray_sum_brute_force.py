def max_subarray_sum(A):
    max_sum = -1*(10000)
    for i in range(len(A)):
        sum = 0
        for j in range(i, len(A)):
            sum = sum + A[j]
            if(sum > max_sum):
                max_sum = sum
    return max_sum

if __name__ == '__main__':
    A = [-2, -5, 6, -2, -3, 1, 5, -6]
    sumA = max_subarray_sum(A)
    print(sumA)
