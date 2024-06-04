# 標準入力及び配列の初期化
N,Q = map(int,input().split())
T = list(map(int,input().split()))
Dent = []

# 配列DentにN個分のTrue(1)を格納
for _ in range(N):
    Dent.append(1)

# 施術配列Tを読み込み、配列Dentに対して処理
for i in range(Q):
    if(Dent[T[i]-1]==1):
        Dent[T[i]-1] = 0
    else:
        Dent[T[i]-1] = 1

# 出力
print(sum(Dent))