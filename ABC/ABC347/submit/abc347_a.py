def function():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = []

    total = 0
    for i in range(N):
        if(A[i]%K == 0):
          B.append(A[i]//K)

    print(*B)


if __name__ == "__main__":
    function()