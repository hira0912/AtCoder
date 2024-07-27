def function():
    N,X,Y = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)

    #配列Aを評価
    a_sum = 0
    for i in range(N):
        a_sum += A[i]
        if(a_sum > X):
            break
    #配列Bを評価
    b_sum = 0
    for j in range(N):
        b_sum += B[j]
        if(b_sum > Y):
            break
    
    print(min(i+1,j+1))
    return

if __name__ == "__main__":
    function()