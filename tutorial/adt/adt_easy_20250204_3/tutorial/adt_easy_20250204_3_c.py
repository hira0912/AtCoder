def function():
    N = str(input())

    if(len(N)<=3):
        print(N)
    else:
        X = '0'*(len(N)-3)
        N = N[0:3]+X
        print(N)

if __name__ == "__main__":
    function()