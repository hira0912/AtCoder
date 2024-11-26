def function():
    S = str(input())

    ret = func_1122k(S)
    if(ret):
        print('Yes')
    else:
        print('No')
    return

def func_1122k(string:str) -> bool:
    num = len(string)
    if(num%2 != 0):
        return False
    else:
        set_string = set()
        for i in range(0,num,2):
            if(string[i]!=string[i+1]):
                return False
            set_string.add(string[i])
        if(len(set_string)!=num/2):
            return False
    return True
        
if __name__ == "__main__":
    function()