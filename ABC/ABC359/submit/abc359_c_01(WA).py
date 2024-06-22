def function():
    S = list(map(int,input().split()))
    T = list(map(int,input().split()))

    ydt = T[1]-S[1]
    xdt = T[0]-S[0]
    if(ydt>=xdt):
        print(ydt)
        return
    
    SLR = (S[0]+S[1])%2
    TLR = (T[0]+T[1])%2
    if(S[0]<=T[0]):
        xk = S[0]
        if(SLR == 0):
            xk += 1
        xk += ydt
        xkLR = (xk+T[1])%2
        if(xkLR==TLR):
            ans = ydt+(T[0]-xk)//2
        elif(xkLR==1 and TLR==0):
            ans = ydt+(T[0]+1-xk)//2
        else:
            ans = ydt+(T[0]-xk-1)//2
        print(ans)
        return

    else:
        xk = T[0]
        if(TLR == 0):
            xk += 1
        xk += ydt
        xkLR = (xk+S[1])%2
        if(xkLR==SLR):
            ans = ydt+(S[0]-xk)//2
        elif(xkLR==1 and SLR==0):
            ans = ydt+(S[0]+1-xk)//2
        else:
            ans = ydt+(S[0]-xk-1)//2
        print(ans)
        return                
    return

if __name__ == "__main__":
    function()