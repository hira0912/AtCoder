def function():
    N,T,P = map(int,input().split())
    L = list(map(int,input().split()))

    for i in range(T):
        ans = 0
        for j in range(N):
            if(L[j] >= T-i):
                ans += 1

        if(ans >= P):
            print(i)
            break
    return

if __name__ == "__main__":
    function()