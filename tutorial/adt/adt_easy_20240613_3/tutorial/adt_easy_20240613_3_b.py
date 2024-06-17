def function():
    S = str(input())
    if(len(S)==1):
        print(S*6)
    elif(len(S)==2):
        print(S*3)
    else:
        print(S*2)
    return

if __name__ == "__main__":
    function()