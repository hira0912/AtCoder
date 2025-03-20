def function():
    N = int(input())

    print('{:0=2}'.format(N%100))
    return

if __name__ == "__main__":
    function()