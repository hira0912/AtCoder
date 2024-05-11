def function():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0

    for i in range(N):
        for j in range(i+1,N):
            ans += (A[i]+A[j])%(10**8)
    
    print(ans)

if __name__ == "__main__":
    function()