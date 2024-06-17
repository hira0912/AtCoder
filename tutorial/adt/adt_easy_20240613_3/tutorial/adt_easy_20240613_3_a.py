def function():
    N = int(input())
    S = str(input())

    flag = 0
    for i in range(N):
        if(S[i]=='|'):
            flag += 1
        
        if(S[i]=='*'):
            if(flag==1):
                print('in')
                return
            else:
                print('out')
                return

if __name__ == "__main__":
    function()