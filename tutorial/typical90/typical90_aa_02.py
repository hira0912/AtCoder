def function():
    S_set = set()
    N = int(input())
    for i in range(N):
        S = str(input())
        if(not S in S_set):
            S_set.add(S)
            print(i+1)

if   __name__ == "__main__":
    function()