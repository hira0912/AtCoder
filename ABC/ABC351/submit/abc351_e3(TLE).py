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
        num = []
        if(len(a)==0):
            return 0
        for i in range(len(a)-1):
            aset_i = a[i]
            for j in range(i+1,len(a)):
                aset_j = a[j]
                dx = abs(aset_i[0]-aset_j[0])
                dy = abs(aset_i[1]-aset_j[1])
                if(dx>dy):
                    num.append(dx)
                    continue
                else:
                    num.append(dy)
        return sum(num)
    
    print(sumup(a1)+sumup(a2))
    return

if __name__ == "__main__":
    function()