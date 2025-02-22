def function():
    S = str(input())
    T = ''
    for i in range(len(S)):
        if(S[i]=='2'):
            T += '2'
    print(T)
    return

if __name__ == "__main__":
    function()