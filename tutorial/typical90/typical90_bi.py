def function():
    Q = int(input())
    yama = []
    for i in range(Q):
        t,x = map(int,input().split())
        if(t==1):
            yama.insert(0,x)
        if(t==2):
            yama.append(x)
        if(t==3):
            print(yama[x-1])

if __name__ == "__main__":
    function()