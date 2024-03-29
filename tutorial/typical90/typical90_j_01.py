N = int(input())
data = []
for i in range(N):
    data.append(str(input()))
Q = int(input())
for j in range(Q):
    question = list(map(int,input().split()))
    score1,score2 = 0,0
    for k in range(question[0]-1,question[1]):
        dstr = data[k].split()
        if(dstr[0] == 1):
            score1 += dstr[1]
        else:
            score2 += dstr[1]
    print("{} {}".format(score1,score2))
