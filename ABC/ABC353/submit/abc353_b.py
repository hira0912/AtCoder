def function():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))

    K_temp = K
    round = 0
    for c in A:
        if(K_temp<c):
            round += 1
            K_temp = K
        
        K_temp -= c
    
    print(round+1)
    return

if __name__ == "__main__":
    function()