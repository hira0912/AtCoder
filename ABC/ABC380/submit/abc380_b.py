def function():
    S = str(input())
    A = []
    cnt = 0
    for i in range(len(S)):
        if i!=0:
            if S[i]=='|':
                A.append(cnt)
                cnt = 0
            else:
                cnt += 1
    
    print(*A)
    return

if __name__ == "__main__":
    function()