def function():
    # 標準入力
    n = int(input())
    a1 = []
    a2 = []

    # x+yの2で割った余りが異なる点同士は到達不可能なので、
    # それらを先に組み分けしておく
    for _ in range(n):
        a = list(map(int,input().split()))
        if((a[0]+a[1])%2 == 0):
            a1.append(a)
        else:
            a2.append(a)

    # 計算関数の定義
    def sumup(a):
        X = []
        Y = []
        num = 0
        for c in range(len(a)):
            X.append(a[c][0]+a[c][1])
            Y.append(a[c][1]-a[c][0])
        X.sort()
        Y.sort()
        XY_len = len(X)
        for i in range(XY_len):
            num += (2*i + 1 - XY_len) * (X[i] + Y[i]) // 2
        return num

    # 結果の出力
    print(sumup(a1) + sumup(a2))
    return

if __name__ == "__main__":
    function()