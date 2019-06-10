INF = 100000
n = 5 // length of the rod
r = [0] + [-1*INF]*5 // defining revenue matrix

def rod_cutting_top_down(cm, n):
    global r
    if r[n] >=0 :
        return r[n]
    maximum_revenue = -1*INF
    for i in range(1, n+1):
        maximum_revenue = max(maximum_revenue, cm[i] + rod_cutting_top_down(cm, n-i))
    r[n] = maximum_revenue
    return r[n]

if __name__ == '__main__':
    # list starting from 1, element at index 0 is fake
    cm = [0, 10, 24, 30, 40, 45]
    print("Maximum revenue is ",rod_cutting_top_down(cm,n))
