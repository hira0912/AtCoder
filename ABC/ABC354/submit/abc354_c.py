def function():
    m = int(input())
    data = []
    for i in range(m):
        k = list(map(int,input().split()))
        k.append(i+1)
        data.append(k)
    
    data.sort(reverse=True)

    x = []
    count = 0
    i = 0
    i_data = 0
    while count < m:
        if(i==0):
            x.append(data[i][2])
            i_data = data[i][1]
            i += 1
        else:
            if(data[i][1] > i_data):
                i += 1
            else:
                x.append(data[i][2])
                i_data = data[i][1]
                i += 1
        
        count += 1

    x.sort()
    
    print(len(x))
    print(*x)

if __name__ == "__main__":
    function()