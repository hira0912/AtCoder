def function():
    N,M = map(int,input().split())
    H = list(map(int, input().split()))

    for i in range(N):
        if(M<H[i]):
            i= i-1
            break
        else:
            M -= H[i]
    print(i+1)
    return

if __name__ == "__main__":
    function()