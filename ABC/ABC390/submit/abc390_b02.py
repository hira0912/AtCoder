def function():
    N = int(input())
    A = list(map(int,input().split()))

    for i in range(1,N):
        if(A[i]*A[0] != A[1]*A[i-1]):
            print('No')
            return
    print('Yes')
    return

if __name__ == "__main__":
    function()