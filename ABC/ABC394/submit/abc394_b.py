def function():
    N = int(input())
    S = []
    for i in range(N):
        inp = str(input())
        if(i==0):
            S.append(inp)
        else:
            flag = 0
            for j in range(len(S)):
                if(len(inp)<len(S[j])):
                    S.insert(j,inp)
                    flag = 1
                    break
            if(flag==0):
                S.append(inp)
    
    ret = ''
    for j in range(len(S)):
        ret += S[j]
    print(ret)
    return

if __name__ == "__main__":
    function()