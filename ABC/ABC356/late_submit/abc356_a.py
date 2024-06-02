def function():
    N,L,R = map(int,input().split())
    A = []
    for i in range(0,L-1):
        A.append(i+1)
    for i in reversed(range(L-1,R)):
        A.append(i+1)
    for i in range(R,N):
        A.append(i+1)
    print(*A)

if __name__ == "__main__":
    function()