def function():
    R,G,B = map(int,input().split())
    C = str(input())
    if(C=='Red'):
        R = 999
    if(C=='Blue'):
        B = 999
    if(C=='Green'):
        G = 999
    print(min(R,G,B))
    return

if __name__ == "__main__":
    function()