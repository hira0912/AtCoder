def function():
    N,K = map(int,input().split())
    R = list(map(int,input().split()))

    val = []
    for _ in range(N):
        val.append(1)
    col = N-1

    while(True):
        if(val[0]>R[0]):
            break
        vsum = sum(val)
        while(val[col]<=R[col]):
            if((vsum%K)==0):
                print(*val)
            val[col] += 1
            vsum += 1

        if(col>1):
            for i in range(col,N):
                val[i]=1
            if(val[col-1] < R[col-1]):
                val[col-1]+=1
                col = N-1
            else:
                val[col-1]+=1
                col -= 1
        else:
            val[0]+=1
            for i in range(1,N):    
                val[i]=1
            col = N-1
    return

if __name__ == "__main__":
    function()