F = [-1] * 50 # Array to store fibonacci terms
def fabonacci_memoization(n):
    if F[n] < 0 :
        if n == 0:
            F[n] = 0
        elif n == 1:
            F[n] = 1
        else:
            F[n] = fabonacci_memoization(n-1) + fabonacci_memoization(n-2)
    return F[n]
if __name__ == '__main__':
    print(fabonacci_memoization(46))
