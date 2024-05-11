import bisect

def function():
    N = int(input())
    A = list(map(int,input().split()))
    B = []
    A.sort()

    for i in range(N):
        if(i==0):
            B.append(A[i])
        else:
            B.append(A[i]+B[i-1])

    ans = 0
    for i in range(N-1):
        a = 10**8 - A[i] -1
        k = bisect.bisect(A[i+1:N],a)
        ans += B[N-1]-B[i]+A[i]*(N-1-i)-(N-k-1-i)*(10**8)
    
    print(ans)
    return

if __name__ == "__main__":
    function()