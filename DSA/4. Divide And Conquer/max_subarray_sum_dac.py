# def max_of_three(a, b, c):
#    if a >= b and a >= c:
#        return a
#    if b >= a and b >= c:
#        return b
#    return c
def max_crossing_sum_subarray(A, low, mid, high):
    left_sum = -100000
    sum = 0
    for i in range(mid, low-1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum

    right_sum = -100000
    sum = 0
    for i in range(mid+1,high+1):
        sum = sum + A[i]
        if sum > right_sum:
            right_sum = sum
    return left_sum + right_sum

def max_sum_subarray(A, low, high):
    if high == low:
        return A[high]
    mid = (low + high)//2
    left_subarray_sum = max_sum_subarray(A, low, mid)
    right_subarray_sum = max_sum_subarray(A, mid+1, high)
    crossing_sum = max_crossing_sum_subarray(A, low, mid, high)
    return max(left_subarray_sum, right_subarray_sum, crossing_sum)

if __name__ == '__main__':
    A = [3, -1, -1, 10, -3, -2, 4]
    print(max_sum_subarray(A,0,6))
