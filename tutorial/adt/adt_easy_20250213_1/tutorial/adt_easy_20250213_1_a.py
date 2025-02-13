def function():
    H,W = map(int,input().split())
    R,C = map(int,input().split())

    tot = 4
    if(R==1):
        tot -= 1
    if(R==H):
        tot -= 1
    if(C==1):
        tot -= 1
    if(C==W):
        tot -= 1
    print(tot)
    return

if __name__ == "__main__":
    function()