# Merging function which is a heart of merge_sort
def merging(A, low, mid, high):
    # Defining two arrays temp1 and temp2 to store value
    # of left half and right half, and finding their size
    size_of_temp1 = (mid-low)+1
    size_of_temp2 = (high - mid) # (high - (mid +1)) +1 = (high - mid)
    # Initializing the temp1 and temp2 with zeros
    temp1 = [0]*size_of_temp1
    temp2 = [0]*size_of_temp2
    # Storing left half values in temp1
    for i in range(0, size_of_temp1):
        temp1[i] = A[low + i]
    # Storing right half values in temp2
    for i in range(0, size_of_temp2):
        temp2[i] = A[mid+1+i]
    # Here we are checking condition and sorting the array and merging them
    i = 0
    j = 0
    k = low
    while (i < size_of_temp1) and (j < size_of_temp2):
        if temp1[i] < temp2[j]:
            A[k] = temp1[i]
            i = i+1
        else:
            A[k] = temp2[j]
            j = j+1
        k = k+1
    while i < size_of_temp1:
        A[k] = temp1[i]
        k = k+1
        i = i+1
    while j < size_of_temp2:
        A[k] = temp2[j]
        k = k+1
        j = i+1

# Merge Sort function using divide and conquer paradigm..
def merge_sort(A, low, high):
    # Checking if array has more than single elements
    if (low < high):
        # if array has indeed, then find middle element and divide the array
        # based on middle element
        mid = (low + high)//2
        # recursively calling merge_sort on left halves
        merge_sort(A, low, mid)
        # Similarly, calling merge_sort on right halves
        merge_sort(A, mid+1, high)
        # Merging the left and right halves based on certain condition of merging
        merging(A, low, mid, high)

# Driven Program to run code
if __name__ == '__main__':
    array = [4, 8, 1, 3, 10, 9, 2, 11, 5, 6]
    print(array)
    merge_sort(array, 0, 9)
    print(array)
