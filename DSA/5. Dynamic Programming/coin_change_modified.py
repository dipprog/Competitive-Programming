INF = 100000
# k is the number of denominations of the coin or length of dm (denomination matrix)
def coin_change_modified(dm, n, k):
    M = [0]*(n+1)
    S = [0]*(n+1)
    for j in range(1, n+1):
        minimum = INF
        coin = 0
        for i in range(1, k+1):
            if j >= dm[i]:
                minimum = min(minimum, 1 + M[j-dm[i]])
                coin = i
        M[j] = minimum
        S[j] = coin
    l = n
    print("Denomination are: ")
    while l > 0 :
        print(d[S[l]])
        l = l - d[S[l]]
    return M[n]

if __name__ == '__main__':
  # array starting from 1, element at index 0 is fake
  d = [0, 1, 2, 3, 4, 5]
  print("Minimum number of denomination needed:",coin_change_modified(d, 15, 5)) #to make 5. Number of denominations = 3
