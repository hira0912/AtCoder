def function():
    # 標準入力
    S = list(map(int,input().split()))
    T = list(map(int,input().split()))

    # 各座標系における距離の計算
    # もし点間距離がx座標系よりy座標系の方が大きければ、y座標の差を出力する
    ydt = abs(T[1]-S[1])
    xdt = abs(T[0]-S[0])
    if(ydt>=xdt):
        print(ydt)
        return
    
    # 点Sと点Tの内、X座標にて小さい方をA、大きい方をBとする
    if(S[0]<=T[0]):
        A = S
        B = T
    else:
        A = T
        B = S

    # 点A,Bをそれぞれ同一タイル内の右側に寄せる
    if(A[0]+A[1])%2 == 0:
        A[0] += 1
    if(B[0]+B[1])%2 == 0:
        B[0] += 1
    
    # 点Aを点Bと同じy軸まで移し、同一タイル内の右側に寄せる
    A[0] += ydt
    if(A[0]+B[1])%2 == 0:
        A[0] += 1

    ans = ydt+(B[0]-A[0])//2
    print(ans)
    return            

if __name__ == "__main__":
    function()