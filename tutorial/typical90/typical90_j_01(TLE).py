# 標準入力及び配列の初期化
N = int(input())
data = []

# 点数情報の配列化
for i in range(N):
    data.append(str(input()))
    # [1 85,2 74,2 49,.....]

# 標準入力
Q = int(input())

# 課題情報の入出力
for j in range(Q):
    question = list(map(int,input().split()))
    score1,score2 = 0,0
    for k in range(question[0]-1,question[1]):
        dstr = list(map(int,data[k].split()))
        if(dstr[0] == 1):
            score1 += dstr[1]
        else:
            score2 += dstr[1]
    print("{} {}".format(score1,score2))
