def function():
    N,Q = map(int,input().split())
    P = []
    H = [1]*N
    for i in range(N):
        P.append(i)

    num = 0
    for _ in range(Q):
        data = list(map(int,input().split()))
        if(data[0]==2):
            print(num)
        else:
            H[P[data[1]-1]] -= 1
            if(H[P[data[1]-1]]==1):
                num -= 1
            P[data[1]-1] = data[2]-1

            H[P[data[1]-1]] += 1
            if(H[P[data[1]-1]]==2):
                num += 1
    return

if __name__ == "__main__":
    function()