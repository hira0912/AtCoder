def function():
    N = int(input())
    str = ""
    for i in range(N):
        if(i+1)%3 != 0 :
            str += "o"
        else:
            str += "x"
    print(str)


if __name__ == "__main__":
    function()