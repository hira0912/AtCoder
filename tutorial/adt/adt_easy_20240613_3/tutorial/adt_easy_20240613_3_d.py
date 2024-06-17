def function():
    N = int(input())
  
    if(N>=pow(10,8) and N<=pow(10,9)-1):
        print((N//pow(10,6))*pow(10,6))
    elif(N>=pow(10,7) and N<=pow(10,8)-1):
        print((N//pow(10,5))*pow(10,5))
    elif(N>=pow(10,6) and N<=pow(10,7)-1):
        print((N//pow(10,4))*pow(10,4))
    elif(N>=pow(10,5) and N<=pow(10,6)-1):
        print((N//pow(10,3))*pow(10,3))
    elif(N>=pow(10,4) and N<=pow(10,5)-1):
        print((N//pow(10,2))*pow(10,2))
    elif(N>=pow(10,3) and N<=pow(10,4)-1):
        print((N//pow(10,1))*pow(10,1))
    else:
        print(N)
    return

if __name__ == "__main__":
    function()