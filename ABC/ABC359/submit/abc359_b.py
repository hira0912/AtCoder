def function():
    N = int(input())
    T = list(map(int,input().split()))
    ans = 0

    for i in range(1,N+1):
        for j in range((2*N)-2):
            if(T[j]==i):
                if(T[j+2]==i):
                    ans += 1
                break
    
    print(ans)
    return

if __name__ == "__main__":
    function()