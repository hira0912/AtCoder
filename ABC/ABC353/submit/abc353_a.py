def function():
    N = int(input())
    H = list(map(int,input().split()))

    H_base = H[0]

    for i in range(1,N):
        if(H[i]>H_base):
            print(i+1)
            return
    
    print(-1)
    return

if __name__ == "__main__":
    function()