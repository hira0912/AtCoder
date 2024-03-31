def function():
    # standard input
    N,A,B = map(int,input().split())
    D = list(map(int,input().split()))

    # D mod(A+B) set again
    for i in range(N):
        D[i] = (D[i])%(A+B)
    
    # remove duplicate 
    D_set = set(D)
    D_mod = list(D_set)
    D_mod.sort()

    # variable initialize
    D = []
    D_set = set()

    # check length
    if(len(D_mod) > A+1):
        print('No')
        return
    
    # append D min value + A and B
    D_mod.append(D_mod[0]+A+B)

    # check difference between adjacent values
    for i in range(1,len(D_mod)):
        if(D_mod[i]-D_mod[i-1] > B):
            print('Yes')
            return
    
    # not meet the conditions
    print('No')    

if __name__ == "__main__":
    function()