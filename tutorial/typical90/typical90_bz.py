def function():
    N,M = map(int,input().split())
    data = []

    for j in range(N):
        data.append(0)

    for i in range(M):
        a,b = map(int,input().split())
        if(a!=b):
            if(a>b):
                data[a-1] += 1
            else:
                data[b-1] += 1
    
    for j in range(N):
        if(data[j]>1):
            data[j] = 0

    print(sum(data))
        

if __name__ == "__main__":
    function()