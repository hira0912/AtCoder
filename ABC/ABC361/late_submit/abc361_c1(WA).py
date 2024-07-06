def function():
    # 標準入力
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()

    # 配列Aの差配列Bを生成
    B = []
    A_bef = A[0]
    for i in range(1,N):
        B.append(A[i]-A_bef)
        A_bef = A[i]
    
    # 差配列の両端を比べ、大きい方を中央に1つ進める
    left_key = 0
    right_key = N-1
    for _ in range(K):
        if(B[left_key]>=B[right_key-1]):
            left_key += 1
        else:
            right_key -= 1
    
    # 出力
    print(A[right_key]-A[left_key])
    return


if __name__ == "__main__":
    function()