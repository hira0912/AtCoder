def function():
    # 標準入力
    n = int(input())
    a1 = []
    a2 = []

    # x+yの2で割った余りが異なる点同士は到達不可能なので、
    # それらを先に組み分けしておく
    for _ in range(n):
        a = list(map(int,input().split()))
        if((a[0]+a[1])%2 == 0):
            a1.append(a)
        else:
            a2.append(a)

    # 計算関数の定義
    def sumup(a):
        num = 0
        if(len(a)==0):
            return 0
        for i in range(len(a)-1):
            for j in range(i+1,len(a)):
                if(abs(a[i][0]-a[j][0]) > abs(a[i][1]-a[j][1])):
                    num += abs(a[i][0]-a[j][0])
                else:
                    num += abs(a[i][1]-a[j][1])
        return num
    
    print(sumup(a1)+sumup(a2))
    return

if __name__ == "__main__":
    function()