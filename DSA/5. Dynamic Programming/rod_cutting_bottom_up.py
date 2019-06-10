INF = 100000
n = 5
r = [0] + [-1 * INF]*n

def rod_cutting_bottom_up(cm, n):
    for j in range(1, n+1):
        maximum_revenue = -1*INF
        for i in range(1, j+1):
            maximum_revenue = max(maximum_revenue, cm[i] + r[j-i])
        r[j] = maximum_revenue
    return r[n]

if __name__ == '__main__':
    # list starting from 1, element at index 0 is fake
    cm = [0, 10, 24, 30, 40, 45]
    print("Maximum revenue is ",rod_cutting_bottom_up(cm,n))
