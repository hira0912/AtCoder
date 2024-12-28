def function():
    K= int(input())
    S= str(input())
    T= str(input())

    if(len(S)==len(T)):
        ret = equal_calc(S,T)
    elif(len(S)>len(T)):
        ret = nonequal_calc(S,T)
    else:
        ret = nonequal_calc(T,S)
    if(ret):
        print('Yes')
    else:
        print('No')
    return

def equal_calc(S:str,T:str)->bool:
    N = len(S)
    num = 0
    for i in range(N):
        if(S[i]!=T[i]):
            if(num > 1):
                return False
            num += 1
    return True

def nonequal_calc(S:str,T:str)->bool:
    N = len(S)
    next = 0
    for i in range(N-1):
        if(S[i]==T[i]):
            next = i
        else:
            break

    if(next==i-1):
        return True
    
    for j in range(N,next,-1):
        if(S[i]!=T[i-1]):
            return False
    return True

if __name__ == "__main__":
    function()