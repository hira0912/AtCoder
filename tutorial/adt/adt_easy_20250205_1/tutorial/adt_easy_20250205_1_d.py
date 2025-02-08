def function():
    S = str(input())

    upper = 0
    for i in range(len(S)):
        if(S[i].isupper()):
            upper += 1
    
    if(upper>len(S)//2):
        print(S.upper())
    else:
        print(S.lower())
    return

if __name__ == "__main__":
    function()