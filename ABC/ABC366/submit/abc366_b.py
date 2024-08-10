def function():
    N = int(input())
    S = []
    height = 0
    for _ in range(N):
        moji = str(input())
        S.append(moji)
        if(len(moji)>height):
            height = len(moji)
    
    for i in range(1,height+1):
        pr = ''
        for j in range(N,0,-1):
            if(len(S[j-1])<i):
                pr = pr + '*'
            else:
                pr = pr + S[j-1][i-1]
        
        for k in range(len(pr),0,-1):
            if(pr[k-1]!='*'):
                break
            pr = pr[0:k-1]
        print(pr)
    
    return

if __name__ == "__main__":
    function()