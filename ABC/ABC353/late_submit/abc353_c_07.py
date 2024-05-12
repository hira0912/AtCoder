import bisect

def function():
    # 標準入力
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()

    # 二分探索により条件を満たす整数組の数を導出
    k = 0
    for i in range(N-1):
        if(A[i] >= 5 * 10**7):
            k += N-1-i
        else:
            a = 10**8 - A[i] -1
            k += N-bisect.bisect(A,a)

    # 総和計算
    ans = sum(A)*(N-1) - (10**8)*k
    print(ans)
    return

if __name__ == "__main__":
    function()