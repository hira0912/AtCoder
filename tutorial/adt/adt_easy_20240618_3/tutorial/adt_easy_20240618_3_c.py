def function():
    X = str(input())

    ans = 'Strong'
    if(X[0]==X[1] and X[0]==X[2] and X[0]==X[3]):
        ans = 'Weak'
    
    def calc(a,b):
        if(int(b)==int(a)+1):
            return True
        if(int(b)==0 and int(a)==9):
            return True
        return False
    
    if(calc(X[0],X[1]) = =True and calc(X[1],X[2]) == True and calc(X[2],X[3]) == True):
        ans = 'Weak'
    print(ans)
    return

if __name__ == "__main__":
    function()