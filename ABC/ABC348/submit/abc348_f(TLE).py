def function():
    N,M = map(int,input().split())
    data = []
    for i in range(N):
        data.append(list(map(int,input().split())))

    all_count = 0
    for i in range(N-1):
        for j in range(i+1,N):
            count = 0
            for k in range(M):
                if(data[i][k]==data[j][k]):
                    count += 1
            if(count%2 == 1):
                    all_count += 1
    print(all_count)

if __name__ == "__main__":
    function()