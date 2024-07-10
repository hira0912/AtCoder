def function():
    S = str(input())
    ans = ''

    for i in range(len(S)):
        if(S[i]!='a' and S[i]!='i' and S[i]!='u' and S[i]!='e' and S[i]!='o'):   
            ans += S[i]
    print(ans)
    return

if __name__ == "__main__":
    function()