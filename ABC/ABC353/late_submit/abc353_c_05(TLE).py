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

    k = 0
    for i in range(N-1):
        a = 10**8 - A[i] -1
        k += bisect.bisect(A[i+1:N],a) + i
        
    ans = sum(A)*(N-1) - ((N-1)**2 - k)*(10**8)
    print(ans)
    return

if __name__ == "__main__":
    function()