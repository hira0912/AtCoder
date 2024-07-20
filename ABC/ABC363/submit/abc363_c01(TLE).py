import itertools

def function():
    N,K = map(int,input().split())
    S = str(input())
    S_list = list(S)
    S_list.sort()
    S_Set = set()
    
    ans = 0
    for v in itertools.permutations(S_list,N):
        S_Set.add(v)

    newS = []
    for v in S_Set:
        newS.append(list(v))

    ans = len(newS)
    for i in range(len(newS)):
        for j in range(len(newS[i])-K+1):
            if(K<=3):
                if(newS[i][j] == newS[i][j+K-1]):
                    ans -= 1
                    break
            elif(K<=5):
                if(newS[i][j] == newS[i][j+K-1] and newS[i][j+1] == newS[i][j+K-2]):
                    ans -= 1
                    break
            elif(K<=7):
                if(newS[i][j] == newS[i][j+K-1] and newS[i][j+1] == newS[i][j+K-2] and newS[i][j+2] == newS[i][j+K-3]):
                    ans -= 1
                    break
            elif(K<=9):
                if(newS[i][j] == newS[i][j+K-1] and newS[i][j+1] == newS[i][j+K-2] and newS[i][j+2] == newS[i][j+K-3] and newS[i][j+3] == newS[i][j+K-4]):
                    ans -= 1
                    break
            else:
                if(newS[i][j] == newS[i][j+K-1] and newS[i][j+1] == newS[i][j+K-2] and newS[i][j+2] == newS[i][j+K-3] and newS[i][j+3] == newS[i][j+K-4] and newS[i][j+4] == newS[i][j+K-5]):
                    ans -= 1
                    break
    print(ans)
    return

if __name__ == "__main__":
    function()