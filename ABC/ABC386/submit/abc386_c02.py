def function():
    K= int(input())
    S= str(input())
    T= str(input())

    if(len(S)==len(T)):
        ret = equal_calc(S,T)
    elif(len(S)-1==len(T)):
        ret = nonequal_calc(S,T)
    elif(len(T)-1==len(S)):
        ret = nonequal_calc(T,S)
    else:
        ret = False
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
            if(num > 0):
                return False
            num += 1
    return True

def nonequal_calc(S:str,T:str)->bool:
    N = len(S)
    next = 0
    for i in range(N-1):
        next = i
        if(S[i]!=T[i]):
            break
    if(next==N-2):
        return True

    for j in range(N-1,next,-1):
        if(S[j]!=T[j-1]):
            return False
    return True

if __name__ == "__main__":
    function()