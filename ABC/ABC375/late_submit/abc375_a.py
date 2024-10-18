def function():
    N = int(input())
    S = str(input())
    ret = 0
    for i in range(N-2):
        if(S[i]=='#' and S[i+1]=='.' and S[i+2]=='#'):
            ret += 1
    print(ret)
    return

if __name__ == "__main__":
    function()