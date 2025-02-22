def function():
    S = str(input())

    flag = 0
    start = 0
    while flag==0:
        flag = 1
        for i in range(start,len(S)-1):
            if(S[i]=='W' and S[i+1]=='A'):
                S = S[:i] + 'AC' + S[i+2:]
                start = i-1
                flag = 0
                break
    print(S)
    return

if __name__ == "__main__":
    function()