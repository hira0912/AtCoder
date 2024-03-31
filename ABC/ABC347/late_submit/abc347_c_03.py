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

    # check difference between the minimum and maximum values
    # if not meet the conditions, add a+b to the minimum value
    for i in range(len(D_mod)):
        if(i==0):
            if(D_mod[len(D_mod)-1] - D_mod[i] < A):
                print('Yes')
                return
            else:
                D_mod[i] += A+B
            continue

        if(D_mod[i-1] - D_mod[i] < A):
            print('Yes')
            return
        else:
            D_mod[i] += A+B
    
    # not meet the conditions
    print('No')    

if __name__ == "__main__":
    function()