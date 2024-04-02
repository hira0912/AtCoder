def function():
    N,P,Q = map(int,input().split())
    A = list(map(int,input().split()))

    if(P==0):
        print(0)
        return

    for i in range(N):
        A[i] = A[i]%P

    count = 0
    for i in range(len(A)-4):
        for j in range(i+1,len(A)-3):
            for k in range(j+1,len(A)-2):
                for l in range(k+1,len(A)-1):
                    for m in range(l+1,len(A)):
                        data = (A[i]*A[j])%P
                        data = (data*A[k])%P
                        data = (data*A[l])%P
                        data = (data*A[m])%P
                        if(data == Q):
                            count += 1
    print(count)

if __name__ == "__main__":
    function()