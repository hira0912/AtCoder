def function():
    S = input()
    for i in range(len(S)):
        if S[i] == 'R':
            print('Yes')
            return
        if S[i] == 'M':
            print('No')
            return
    return        

if __name__ == "__main__":
    function()