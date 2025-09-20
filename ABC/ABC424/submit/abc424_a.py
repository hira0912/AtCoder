def function():
    A,B,C = map(int,input().split())

    if A==B or B==C or A==C:
        print("Yes")
    else:
        print("No")
    return

if __name__ == "__main__":
    function()