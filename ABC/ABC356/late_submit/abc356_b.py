def function():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = []
    for _ in range(M):
        B.append(0)
    
    for _ in range(N):
        c = list(map(int,input().split()))
        for i in range(M):
            B[i] += c[i]
    
    ans = 'Yes'
    for i in range(M):
        if(A[i] > B[i]):
            ans = 'No'
            break
    print(ans)

if __name__ == "__main__":
    function()