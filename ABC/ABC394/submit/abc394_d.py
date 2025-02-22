from collections import deque

def function():
    S = str(input())
    T = deque()
    data = ['<','(','[']
    check = ['<>','()','[]']

    ret = 'Yes'
    for i in range(len(S)):
        if(S[i] in data):
            T.append(S[i])
        else:
            if(len(T)==0):
                ret = 'No'
                break
            k = T.pop()+S[i]
            if(k not in check):
                ret = 'No'
                break
    if(len(T)!=0):
        ret = 'No'
    
    print(ret)
    return

if __name__ == "__main__":
    function()