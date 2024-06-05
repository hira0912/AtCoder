def function():
    N,M,K = map(int,input().split())
    C,A,R = [],[],[]
    for _ in range(M):
        c,*a,r = input().split()
        C.append(c)
        A.append([int(i)-1 for i in a])
        R.append(r)

    ans = 0
    for i in range(2**N):
        bt = bin(i)
        btz = bt[2:len(bt)].zfill(N)
        cnt = 0
        for c in range(len(btz)):
            if(btz[c])=='1':
                cnt += 1
        if(cnt!=K):
            continue
        for j in range(M):
            


if __name__ == "__main__":
    function()