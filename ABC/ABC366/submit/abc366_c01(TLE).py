def function():
    Q = int(input())
    ball = []

    for _ in range(Q):
        query = list(map(int,input().split()))
        if(query[0]==1):
            ball.append(query[1])
        if(query[0]==2):
            ball.sort()
            ball.remove(query[1])
        if(query[0]==3):
            ball.sort()
            ball_set = set(ball)
            print(len(ball_set))
    return

if __name__ == "__main__":
    function()