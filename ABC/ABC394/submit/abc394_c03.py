def function():
    S = str(input())
    T = []

    for i in range(len(S)-1):
        if(S[i]=='W'):
            T.append(i)

    stock = 0
    for i in range(len(T)):
        if(i!=len(T)-1):
           if(T[i+1]==T[i]+1):
            stock += 1
            continue
        if(S[T[i]+1]=='A'):
            S = S[0:(T[i]-stock)] + 'A' + 'C'*(stock+1) + S[T[i]+2:]
            stock = 0
        else:
            stock = 0
    print(S)
    return

if __name__ == "__main__":
    function()