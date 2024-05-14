import bisect

def function():
    # 標準入力
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()

    # 二分探索で導出
    k = 0
    for i in range(N-1):
        a = 10**8 - A[i] -1
        k += bisect.bisect(A[i+1:N],a) + i
        
    ans = sum(A)*(N-1) - ((N-1)**2 - k)*(10**8)
    print(ans)
    return

if __name__ == "__main__":
    function()