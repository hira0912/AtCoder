import math
def function():
    N = int(input())
    X = []
    Y = []
    X.append(0)
    Y.append(0)
    for i in range(N):
        inpX,inpY = map(int,input().split())
        X.append(inpX)
        Y.append(inpY)

    sum = 0
    for i in range(N+1):
        if(i!=N):
            sum += math.sqrt(abs(X[i+1]-X[i])**2 + abs(Y[i+1]-Y[i])**2)
        else:
            sum += math.sqrt(abs(X[0]-X[i])**2 + abs(Y[0]-Y[i])**2)            
    print(sum)
    return

if __name__ == "__main__":
    function()