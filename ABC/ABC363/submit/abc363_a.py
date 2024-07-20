def function():
    R = int(input())
    if(R>=200):
        print(300-R)
    elif(R>=100):
        print(200-R)
    else:
        print(100-R)
    return

if __name__ == "__main__":
    function()