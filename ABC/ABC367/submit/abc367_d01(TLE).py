def function():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    for i in range(len(A)):
        if(A[i]>M):
            A[i] = A[i] % M

    ans = 0
    for i in range(N):
        roop = 0
        tot = 0
        while(roop < N-1):
            tot += A[(i+roop)%N]
            tot = tot%M
            if(tot == 0):
                ans += 1
            roop += 1
    
    print(ans)
    return

if __name__ == "__main__":
    function()