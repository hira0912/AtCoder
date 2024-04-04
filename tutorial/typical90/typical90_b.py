from itertools import product

def function():
    N = int(input())
    if(N%2 != 0):
        return
    
    data = []
    for S in product(["(",")"],repeat=N):
        S= ''.join(S)
        c1 = S
        c2 = ""
        while c1 != c2:
            c2 = c1
            c1 = c1.replace("()","")
        if c1 == "":
            data.append(S)
    
    data.sort
    for c in data:
        print(c)

if   __name__ == "__main__":
    function()