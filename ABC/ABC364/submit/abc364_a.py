def function():
    N = int(input())
    for i in range(N-1):
        inp = str(input())
        if(i!=0):
            if(inp_old == 'sweet' and inp == 'sweet'):
                print('No')
                return
        inp_old = inp
    print('Yes')
    return

if __name__ == "__main__":
    function()