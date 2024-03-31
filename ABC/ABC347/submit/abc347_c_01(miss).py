def function():
    N,A,B = map(int,input().split())
    D = list(map(int,input().split()))
    for i in range(N):
        D[i] = (D[i])%(A+B)
    
    if(max(D)-min(D) < A):
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    function()