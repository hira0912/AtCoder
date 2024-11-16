def function():
    N = str(input())
    i1 = 0
    i2 = 0
    i3 = 0
    for i in range(len(N)):
        if(N[i]=='1'):
            i1 += 1
        if(N[i]=='2'):
            i2 += 1
        if(N[i]=='3'):
            i3 += 1
    if(i1==1 and i2==2 and i3==3):
        print('Yes')
    else:
        print('No')
    return

if __name__ == "__main__":
    function()