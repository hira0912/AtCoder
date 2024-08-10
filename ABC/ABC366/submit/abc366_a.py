def function():
    N,T,A = map(int,input().split())
    amari = N-T-A
    if(min(T,A)+amari < max(T,A)):
        print('Yes')
    else:
        print('No')
    return
if __name__ == "__main__":
    function()