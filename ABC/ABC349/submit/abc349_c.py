def function():
    S = str(input())
    T = str(input()).lower()

    if(T[2] == 'x'):
        if(T[0] in S and T[1] in S == False):
            print('No')
            return
    else:
        if(T[0] in S and T[1] in S and T[2] in S == False):
            print('No')
            return

    num1 = S.find(T[0])
    if(num1 == -1):
            print('No')
            return

    num2 = S.find(T[1],num1+1)
    if(num2 == -1):
            print('No')
            return
    
    if(T[2] == 'x'):
         print('Yes')
         return

    num3 = S.find(T[2],num2+1)
    if(num3 == -1):
            print('No')
            return
    print('Yes')
    return


if __name__ == "__main__":
    function()