def function():
    N = int(input())
    A = list(map(int,input().split()))

    k = A[1]/A[0]
    for i in range(1,N):
        if(A[i]/A[i-1] != k):
            print('No')
            return
    print('Yes')
    return

if __name__ == "__main__":
    function()