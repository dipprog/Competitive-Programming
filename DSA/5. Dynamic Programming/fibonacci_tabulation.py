F = [-1]*50 # Array to store fibonacci terms
def fibonacci_tabulation(n):
    F[0] = 0
    F[1] = 1
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]
if __name__ == '__main__':
    print(fibonacci_tabulation(40))
