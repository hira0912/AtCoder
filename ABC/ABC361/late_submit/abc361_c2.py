def function():
    # 標準入力
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()

    # 初期区間設定
    ans = 10**9
    left_key = 0
    right_key = N-K-1

    # 区間を右に１個ずつずらす
    while(right_key < N):
        if(A[right_key]-A[left_key] < ans):
            ans = A[right_key]-A[left_key]
        left_key += 1
        right_key += 1
    
    # 出力
    print(ans)
    return

if __name__ == "__main__":
    function()