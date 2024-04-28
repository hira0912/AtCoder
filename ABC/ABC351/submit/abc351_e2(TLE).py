from sys import stdin

def function():
    n = int(stdin.readline())
    a1 = []
    a2 = []

    for _ in range(n):
        a = list(map(int,stdin.readline().split()))
        if((a[0]+a[1])%2 == 0):
            a1.append(a)
        else:
            a2.append(a)

    def sumup(a):
        num = 0
        if(len(a)==0):
            return 0
        for i in range(len(a)-1):
            aset_i = a[i]
            for j in range(i+1,len(a)):
                dx = abs(aset_i[0]-a[j][0])
                dy = abs(aset_i[1]-a[j][1])
                if(dx>=dy):
                    num += dx
                else:
                    num += dy
        return num
    
    print(sumup(a1)+sumup(a2))
    return

if __name__ == "__main__":
    function()