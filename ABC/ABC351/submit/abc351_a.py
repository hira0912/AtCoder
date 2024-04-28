def function():
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    print(sum(a)-sum(b)+1)

if __name__ == "__main__":
    function()