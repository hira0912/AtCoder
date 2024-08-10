def function():
    Q = int(input())
    ball = [0] * 1000001
    ball_count = 0

    for _ in range(Q):
        t,*x = map(int,input().split())
        if(t==1):
            ball[x[0]]+=1
            if(ball[x[0]]==1):
                 ball_count += 1
        elif(t==2):
            ball[x[0]]-=1
            if(ball[x[0]]==0):
                 ball_count -= 1
        else:
            print(ball_count)
    return

if __name__ == "__main__":
    function()