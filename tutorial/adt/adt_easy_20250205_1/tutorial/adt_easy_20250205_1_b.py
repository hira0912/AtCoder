def function():
    N,K,A = map(int,input().split())
    ret = ((K-1) % N + A) % N 
    if(ret==0):
        ret += N
    print(ret)
    return 

if __name__ == "__main__":
    function()