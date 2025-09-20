def function():
    N,M,K = map(int,input().split())
    A = []
    ans = []
    for _ in range(N):
        A.append(0)

    for _ in range(K):
        a,b = map(int,input().split())
        A[a-1] = A[a-1]+1
        if(A[a-1]) == M:
            ans.append(a)

    if(len(ans)!=0):
        print(*ans)

if __name__ == "__main__":
    function()