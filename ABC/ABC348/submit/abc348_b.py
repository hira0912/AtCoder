def function():
    N = int(input())
    Xi = []
    Yi = []
    for i in range(N):
        X,Y = map(int,input().split())
        Xi.append(X)
        Yi.append(Y)

    for i in range(N):
        length = 0
        num = 0
        for j in range(N):
            if(i==j):
                calc = 0
            else:
                calc = abs(Xi[i]-Xi[j])**2 + abs(Yi[i]-Yi[j])**2 
            if(calc > length):
                length = calc
                num = j
        print(num+1)

if __name__ == "__main__":
    function()