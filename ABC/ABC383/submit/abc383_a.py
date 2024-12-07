def function():
    N = int(input())
    sum = 0
    time = 0
    for i in range(N):
        a,b = map(int,input().split())
        sum -= a-time
        if(sum<0):
            sum = 0
        sum += b
        time = a
    print(sum)
    return

if __name__ == "__main__":
    function()