def function():
    X = str(input())
    while(True):
        if(X[-1]=='.'):
            X = X[:-1]
            break
        if(X[-1]=='0'):
            X = X[:-1]
            continue
        break
    print(X)
    return

if __name__ == "__main__":
    function()