def function():
    N,M = map(int,input().split())
    S = []
    T = []

    for _ in range(N):
        S.append(str(input()))
    for _ in range(M):
        T.append(str(input()))
    
    flag1 = 0 #発見フラグ
    flag2 = 1 #結果フラグ ON=OK OFF=NG
    flag3 = 1 #途中終了フラグ ON=OK OFF=NG
    i=0
    j=0
    for i in range(N-M+1):
        for j in range(N-M+1):
            flag2 = 1
            flag3 = 1
            for k in range(M):
                for l in range(M):
                    if(T[k][l]!=S[i+k][j+l]):
                        flag2 = 0
                        flag3 = 0
                        break
                if(flag3!=1):
                   break
            if(flag2==1):
                flag1=1
                break
        if(flag1==1):
            break
    print(i+1,j+1)
    return

if __name__ == "__main__":
    function()