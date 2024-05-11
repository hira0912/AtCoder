def function():
    # 標準入力と配列の昇順ソート
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()

    # 条件を満たす整数組を尺取り法で導出
    k = 0
    left = 0
    right = N-1
    while True:
        if(left >= N-1):
            break
        if(A[left]>= 5*10**7):
            k += N-left-1
            left += 1
            continue
        while True:
            if(A[left]+A[right] < 10**8):
                k += N-right-1
                break
            right -= 1
            continue
        left += 1
        continue

    # 結果の導出
    ans = sum(A)*(N-1) - (10**8)*k
    print(ans)
    return

if __name__ == "__main__":
    function()