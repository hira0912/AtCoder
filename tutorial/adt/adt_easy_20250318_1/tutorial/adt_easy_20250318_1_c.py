def function():
    N,M = map(int,input().split())
    S = []
    T = []
    for _ in range(N):
        S.append(str(input())[3:])
    
    for _ in range(M):
        T.append(str(input()))

    total:int = 0
    for i in range(N):
        for j in range(M):
            if(S[i]==T[j]):
                total += 1
                break
    
    print(total)
    return

if __name__ == "__main__":
    function()