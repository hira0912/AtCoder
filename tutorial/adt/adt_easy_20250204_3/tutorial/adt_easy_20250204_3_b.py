def function():
    A,B,D = map(int,input().split())

    K = []
    for i in range(A,B+D,D):
        K.append(i)
    
    print(*K)

if __name__ == "__main__":
    function()