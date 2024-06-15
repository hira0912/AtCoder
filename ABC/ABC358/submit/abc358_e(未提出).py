import math
def function():

    K = int(input())
    C = list(map(int,input().split()))
    maxC = 0
    malC = 1
    divval = 998244353
    ans = 0

    for ci in C:
        maxC += ci
        if(ci!=0):
            malC *= ci
    if K > maxC:
        K = maxC
    
    for i in range(1,K+1):
        ans += (math.perm(maxC,i)//malC)%divval
        ans = ans%divval
    
    print(ans)
    return



if __name__ == "__main__":
    function()