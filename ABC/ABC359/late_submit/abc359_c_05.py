def function():
    # 標準入力
    S = list(map(int,input().split()))
    T = list(map(int,input().split()))

    # 各座標系における距離の計算
    dy = abs(T[1]-S[1])
    dx = abs(T[0]-S[0])

    # もし点間距離がx座標系よりy座標系の方が大きければ、y座標の差を出力する
    if(dy>=dx):
        print(dy)
        return

    # 各点の左右位置を格納
    S_LR = (S[0]+S[1])%2
    T_LR = (T[0]+T[1])%2

    # 点Sが点Tより左側にある場合
    if(S[0]<=T[0]):
        # 点Sの初期位置がタイルの左側の場合、右側に寄せる
        newPoint_x = S[0]
        if(S_LR == 0):
            newPoint_x += 1

        # 点Tの初期位置がタイルの左側の場合、右側に寄せる
        if(T_LR == 0):
            T[0] += 1

        # y軸を点Tの位置まで動かし、右側に寄せる
        newPoint_x += dy
        newPoint_LR = (newPoint_x + T[1])%2
        if(newPoint_LR == 0):
            newPoint_x += 1

        # 通過タイル数を算出して出力
        ans = (T[0]-newPoint_x)//2 + dy
        print(ans)
        return

    # 点Tが点Sより左側にある場合
    else:
        # 点Tの初期位置がタイルの左側の場合、右側に寄せる
        newPoint_x = T[0]
        if(T_LR == 0):
            newPoint_x += 1

        # 点Sの初期位置がタイルの左側の場合、右側に寄せる
        if(S_LR == 0):
            S[0] += 1

        # y軸を点Sの位置まで動かし、右側に寄せる
        newPoint_x += dy
        newPoint_LR = (newPoint_x + S[1])%2

        # 通過タイル数を算出して出力
        ans = (S[0]-newPoint_x)//2 + dy
        print(ans)
        return
    return

if __name__ == "__main__":
    function()