def function():
    N = int(input())
    W = []
    X = []
    for _ in range(N):
        data = list(map(int,input().split()))
        W.append(data[0])
        X.append([data[1]+9,data[1]+18])

    total = 0
    for tim in range(24):
        num = 0
        for i in range(N):
            if(X[i][0]<=tim and X[i][1]>tim or X[i][0]<=tim+24 and X[i][1]>tim+24):
                num += W[i]
        if(num>total):
            total = num

    print(total)
    return

if __name__ == "__main__":
    function()