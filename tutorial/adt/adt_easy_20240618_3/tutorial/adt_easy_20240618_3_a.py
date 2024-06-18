def function():
    S = str(input())

    if(S[0]==S[1] and S[0]==S[2]):
        print('-1')
        return
    if(S[0]!=S[1] and S[0]!=S[2]):
        print(S[0])
        return
    if(S[0]!=S[1] and S[1]==S[2]):
        print(S[0])
        return
    if(S[0]==S[1] and S[1]!=S[2]):
        print(S[2])
        return
    print(S[1])
    return

if __name__ == "__main__":
    function()