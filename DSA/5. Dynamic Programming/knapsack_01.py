# if n is total number of item and w is weight limit
# then we can write --- cost =[[0 for y in range(w)]for x in range(n)]
# Bottom Up (TABULIZATION) Solution...
n, W = 4, 5
cost= [[0 for y in range(W+1)] for x in range(n+1)]
def knapsack_01(n,W,wm,vm):
    for i in range(1,n+1):
        for w in range(1,W+1):
            if wm[i] > w :
                cost[i][w] = cost[i-1][w]
            else:
                if (vm[i] + cost[i-1][w-wm[i]]) > cost[i-1][w]:
                    cost[i][w] = vm[i] + cost[i-1][w-wm[i]]
                else:
                    cost[i][w] = cost[i-1][w]
    return cost[n][W]
# Items included in optimal solution
def items_in_optimal_solution(n,W, wm):
    i = n
    w = W
    while i > 0 and w > 0 :
        if cost[i][w] != cost[i-1][w]:
            print(i)
            w = w - wm[i]
            i = i-1
        else:
            i = i-1
if __name__ == '__main__':
    # element at index zero is fake. matrix is starting from 1..
    wm = [0, 3, 2, 4, 1]
    vm = [0, 8, 3, 9, 6]

    print("Optimal Value is:",knapsack_01(n, W, wm, vm))
    print("Items included in optimal solution:")
    items_in_optimal_solution(n,W,wm)
