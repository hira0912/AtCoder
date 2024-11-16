def function():
    N,K = map(int,input().split())
    S = str(input())

    first_mode = int(S[0])
    end_mode = int(S[-1])
    mode = first_mode
    R0 = []
    R1 = []
    num = 0

    for i in range(N):
        if(mode==1 and S[i]=='0'):
            R1.append(num)
            mode = 0
            num = 1
        elif(mode==0 and S[i]=='1'):
            R0.append(num)
            mode = 1
            num = 1
        else:
            num += 1
    if(mode==0):
        R0.append(num)
    else:
        R1.append(num)


    #print(*R0)
    #print(*R1)

    if(len(R0)>K):
        R0[K-1] = R0[K-1]+R0[K-0]
        del R0[K]

    R1[K-2] = R1[K-2]+R1[K-1]
    del R1[K-1]

    #print(*R0)
    #print(*R1)

    S=''
    mode = first_mode
    check = True
    cnt = 0
    while(True):
        if(mode==0):
            if(len(R0)<=cnt):
                break
            S += '0' * R0[cnt]
            if(first_mode!=mode):
                cnt += 1
            mode = 1
        else:
            if(len(R1)<=cnt):
                break
            S += '1' * R1[cnt]
            if(first_mode!=mode):
                cnt += 1
            mode = 0
    print(S)    
    return

if __name__ == "__main__":
    function()