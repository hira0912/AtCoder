def function():
    N,K = map(int,input().split())
    S = str(input())

    cnt = 0
    dt = 0
    start_Kmin = 0
    start_Kmax = 0
    end_Kmin = 0
    end_Kmax = 0
    for i in range(N):
        if(dt==0 and S[i]=='1'):
            dt = 1
            cnt += 1
            if(cnt==K-1):
                start_Kmin = i
            elif(cnt==K):
                start_Kmax = i
        if(dt==1 and S[i]=='0'):
            dt = 0
            if(cnt==K-1):
                end_Kmin = i-1
            elif(cnt==K):
                end_Kmax = i-1
    if(end_Kmax==0):
        end_Kmax = i

    #print(start_Kmin)
    #print(end_Kmin)
    #print(start_Kmax)
    #print(end_Kmax)
    Smod = S[0:end_Kmin+1] + S[start_Kmax:end_Kmax+1] + S[end_Kmin+1:start_Kmax] + S[end_Kmax+1:N+1]
    print(Smod)
    return

if __name__ == "__main__":
    function()