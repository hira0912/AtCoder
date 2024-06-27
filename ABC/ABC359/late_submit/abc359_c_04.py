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
    
    # 点Sと点Tの内、X座標にて小さい方をPoint_L、大きい方をPoint_Rとする
    if(S[0]<=T[0]):
        Point_L = S
        Point_R = T
    else:
        Point_L = T
        Point_R = S

    # 点Point_L,Point_Rをそれぞれ同一タイル内の右側に寄せる
    if(Point_L[0]+Point_L[1])%2 == 0:
        Point_L[0] += 1
    if(Point_R[0]+Point_R[1])%2 == 0:
        Point_R[0] += 1
    
    # 点Point_Lから点Point_Rと同じy軸まで移動し、その後同一タイル内の右側に寄せる
    Point_L[0] += dy
    if(Point_L[0]+Point_R[1])%2 == 0:
        Point_L[0] += 1

    # x軸の差分の半分とy軸の移動分の和を出力
    ans = (Point_R[0]-Point_L[0])//2 + dy
    print(ans)
    return            

if __name__ == "__main__":
    function()