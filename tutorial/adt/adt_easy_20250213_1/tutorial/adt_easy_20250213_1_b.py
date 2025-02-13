def function():
    S,T,X = map(int,input().split())
    X += 0.5
    ret = 'No'
    if(S<T):
        if(X>S and X<T):
            ret = 'Yes'
    else:
        if(X>0 and X<T or X>S and X<24):
            ret = 'Yes'        
    print(ret)
    return

if __name__ == "__main__":
    function()