def function():
    S = str(input())
    T = ''
    for i in range(len(S)):
        if(i%2!=0):
            T += S[i] + S[i-1]
    print(T)
    return

if __name__ == "__main__":
    function()