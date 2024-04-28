def function():
    n = int(input())
    a = list(map(int,input().split()))
    c = []

    for i in range(n):
        c.append(a[i])
        while(True):
            if(len(c)==1 or c[-1] != c[-2]):
                break
            if(c[-1] == c[-2]):
                c[-2] += 1
                del c[-1]
                
    print(len(c))   

if __name__ == "__main__":
    function()