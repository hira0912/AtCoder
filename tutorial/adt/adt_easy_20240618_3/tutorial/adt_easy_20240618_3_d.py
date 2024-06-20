def function():
    N,K = map(int,input().split())
    S = []

    for _ in range(N):
        S.append(input())

    S.sort()
    ans = 0
    while True:
        if ans == 1:
            break
        ans = 0
        for i in range(N-1):
            if(len(S[i]) >= len(S[i+1])):
                for j in range(len(S[i+1]))


    for i in range(K):
        print(S[i])

if __name__ == "__main__":
    function()