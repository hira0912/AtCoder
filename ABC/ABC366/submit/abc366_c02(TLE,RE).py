def function():
    Q = int(input())
    ball = []
    query_list = []
    kari_ball_app = []
    kari_ball_del = []

    for _ in range(Q):
        query = list(map(int,input().split()))
        if(query[0]<3):
            query_list.append(query)
        else:
            sorted(query_list, key=lambda x: x[0])
            sorted(query_list, key=lambda x: x[1])
            for c in query_list:
                if(c[0]==1):
                    kari_ball_app.append(c[1])
                else:
                    if(c[1] in kari_ball_app ==True):
                        kari_ball_app.remove(c[1])
                    else:
                        kari_ball_del.append(c[1])

            ball.sort()
            for d in kari_ball_del:
                ball.remove(d)
            ball += kari_ball_app

            ball.sort()
            ball_set = set(ball)
            print(len(ball_set))

            kari_ball_app.clear()
            kari_ball_del.clear()
            query_list.clear()
    return

if __name__ == "__main__":
    function()