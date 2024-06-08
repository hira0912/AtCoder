def function():
    S = str(input())
    cnt = 0
    for i in range(len(S)):
        if S[i].isupper() == True:
            cnt += 1
        else:
            cnt -= 1
    
    if cnt > 0:
        print(S.upper())
    else:
        print(S.lower())
    return

if __name__ == "__main__":
    function()