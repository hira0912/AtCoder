def function():
    N,A = map(int,input().split())
    T = list(map(int,input().split()))

    tim = 0
    for c in T:
        if(c>tim):
            tim = c
        tim += A
        print(tim)
    return

if __name__ == "__main__":
    function()