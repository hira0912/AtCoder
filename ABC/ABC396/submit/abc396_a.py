def function():
    N = int(input())
    A = list(map(int,input().split()))

    for i in range(N-2):
        if(A[i]==A[i+1] and A[i]==A[i+2]):
            print('Yes')
            return
    print('No')
    return

if __name__ == "__main__":
    function()