def function():
    Q = int(input())
    ball = [0] * 1000000
    ball_count = 0

    for _ in range(Q):
        query = list(map(int,input().split()))
        if(query[0]==1):
            ball[query[1]]+=1
            if(ball[query[1]]==1):
                 ball_count += 1
        if(query[0]==2):
            ball[query[1]]-=1
            if(ball[query[1]]==0):
                 ball_count -= 1
        if(query[0]==3):
            print(ball_count)
    return

if __name__ == "__main__":
    function()