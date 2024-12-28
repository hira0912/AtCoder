def function():
    S = str(input())

    num = 0
    for i in range(1,len(S)):
        if(S[i]=='0' and S[i-1]=='0'):
            num += 1
            S = S[:i] + '@' + S[i+1:]
    print(len(S)-num)

if __name__ == "__main__":
    function()