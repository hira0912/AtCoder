N = int(input())
data = []

for i in range(N):
    dt = list(map(int,input().split()))
    if(i==0):
        if(dt[0]==1):
            data.append([dt[1],0])

        else:
            data.append([0,dt[1]])
    else:
        if(dt[0]==1):
            data.append([data[i-1][0]+dt[1],data[i-1][1]])
        else:
            data.append([data[i-1][0],data[i-1][1]+dt[1]])

Q = int(input())
for j in range(Q):
    question = list(map(int,input().split()))
    score1,score2 = 0,0
    if(question[0]==1):
        score1 = data[question[1]-1][0]
        score2 = data[question[1]-1][1]
    else:
        score1 = data[question[1]-1][0] - data[question[0]-2][0]
        score2 = data[question[1]-1][1] - data[question[0]-2][1] 

    print("{} {}".format(score1,score2))
