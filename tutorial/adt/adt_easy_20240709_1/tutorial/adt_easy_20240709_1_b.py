def function():
    X = int(input())

    if(X>=90):
        print('expert')
    elif(X>=70):
        print(90-X)
    elif(X>=40):
        print(70-X)
    else:
        print(40-X)
    return

if __name__ == "__main__":
    function()