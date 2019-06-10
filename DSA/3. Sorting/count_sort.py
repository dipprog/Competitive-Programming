# Assume that the maximum element that can be in the array is K.
# Now take an Aux[] array of size K+1.
# A[] = array to be sorted.
# sortedA[] = sorted version of A[].
def counting_sort(A):
    maximum = max(A)
    Aux= [0]*(maximum+1)
    sortedA = []
    for i in range(len(A)):
        Aux[A[i]] = Aux[A[i]] + 1
    for i in range(maximum+1):
        if Aux[i] != 0:
            temp = Aux[i]
            while temp > 0 :
                sortedA.append(i)
                temp = temp - 1
    return sortedA

if __name__ == '__main__':
    A = [20,20,20,10,10,9,8,7,7,7,6,2,1,1,1]
    print(A)
    result = counting_sort(A)
    print(result)
