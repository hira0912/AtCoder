import itertools

def function():
    N,M = map(int,input().split())
    S = []

    for _ in range(N):
        S.append(input().split())

    for ans in range(1,N+1):
        comb = []
        for c in itertools.combinations(S,ans):
            comb.append(list(c))
            
        for a in comb:
            check = 'x'*M
            for i in range(len(a)):
                for j in range(len(a[i])):
                    for k in range(len(a[i][j])):
                        if(a[i][j][k] == 'o'):
                            if(k==0):
                                check = 'o' + check[1:]
                            elif(k==M-1):
                                check = check[:M-1] + 'o'
                            else:
                                check = check[:k] + 'o' + check[k+1:]
            if check == 'o'*M:
                print(ans)
                return
    print(ans)
    return


if __name__ == "__main__":
    function()