import math

def function():
    H,W = map(int,input().split())
    if(H == 1 or W == 1):
        print(H*W)
    else:
        print(math.ceil(H/2) * math.ceil(W/2))

if __name__ == "__main__":
    function()