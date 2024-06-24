def function():
    S = list(map(int,input().split()))
    T = list(map(int,input().split()))

    ydt = abs(T[1]-S[1])
    xdt = abs(T[0]-S[0])
    if(ydt>=xdt):
        print(ydt)
        return
    
    if(S[0]>=T[0]):
        A = S
        B = T
    else:
        A = T
        B = S

    if(A[0]+A[1])%2 == 0:
        A[0] += 1

    if(B[0]+B[1])%2 == 0:
        B[0] += 1

    A[0] += ydt
    if(A[0]+B[1])%2 == 0:
        A[0] += 1

    ans = ydt+(B[0]-A[0])//2
    print(ans)
    return            

if __name__ == "__main__":
    function()