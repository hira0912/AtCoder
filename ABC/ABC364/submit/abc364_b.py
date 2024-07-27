def function():
    H,W = map(int,input().split())
    Si,Sj = map(int,input().split())
    C = []
    for i in range(H):
        C.append(str(input()))

    Si = Si-1
    Sj = Sj-1

    X = str(input())
    for xr in range(len(X)):
        Ski = Si
        Skj = Sj
        if(X[xr]!='U' and X[xr]!='D' and X[xr]!='L' and X[xr]!='R'):
            continue
        if(X[xr]=='U'):
            Ski -= 1
            if(Ski < 0 or Ski > H-1):
                continue
        
        if(X[xr]=='D'):
            Ski += 1
            if(Ski < 0 or Ski > H-1):
                continue

        if(X[xr]=='L'):
            Skj -= 1
            if(Skj < 0 or Skj > W-1):
                continue

        if(X[xr]=='R'):
            Skj += 1
            if(Skj < 0 or Skj > W-1):
                continue

        if(C[Ski][Skj]=='.'):
            Si = Ski
            Sj = Skj
        
    print(Si+1,Sj+1)  
    return      

if __name__ == "__main__":
    function()