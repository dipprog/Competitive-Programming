def divide_and_conquer(A,beg,end):
    if(beg < end):
        mid = (beg + end)//2
        divide_and_conquer(A,beg,mid)
        divide_and_conquer(A,mid+1,end)
    else:
        A[beg] = A[beg]+1

if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9]
    divide_and_conquer(A,0,8)
    print(A)
