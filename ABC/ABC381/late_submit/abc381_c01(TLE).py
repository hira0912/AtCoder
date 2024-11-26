def function():
    N = int(input())
    S = str(input())
    slash_points = string_check(N,S)
    max_string = 0
    for slash_point in slash_points:
        score = 0
        for i in range(min(slash_point,N-slash_point-1)):
            score = i
            ret = func_1122(2*i+1,S[slash_point-i:slash_point+i+1])
            if(ret==False):
                score = i-1
                break
        if(2*score+1 > max_string):
            max_string = 2*score+1
    print(max_string)
    return

def string_check(num:int, string:str) -> list:
    slash_point = []
    for i in range(num):
        if(string[i]=='/'):
            slash_point.append(i)
    return slash_point

def func_1122(num:int, string:str) -> bool:
    if(string[0:(num//2)]==(num//2)*'1' and string[num//2+1:num]==(num//2)*'2'):
        return True
    else:
        return False
        

if __name__ == "__main__":
    function() 