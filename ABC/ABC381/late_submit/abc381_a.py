def function():
    N = int(input())
    S = str(input())

    ret = func_1122(N,S)
    if(ret):
        print('Yes')
    else:
        print('No')
    return

def func_1122(num:int, string:str) -> bool:
    if(num%2 == 0):
        return False
    elif(num//2 < 1):
        if(string[0]=='/'):
            return True
        else:
            return False
    else:
        if(string[0:(num//2)]==(num//2)*'1' and string[num//2]=='/' and string[num//2+1:num]==(num//2)*'2'):
            return True
        else:
            return False
        

if __name__ == "__main__":
    function()