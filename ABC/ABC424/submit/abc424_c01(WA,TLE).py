def function():
    N = int(input())
    A = []
    B = []
    ans = 0

    for i in range(N):
        a,b = map(int,input().split())
        if(a==0 and b==0):
            A.append(i)
        else:
            Ba = [i,a-1,b-1]
            B.append(Ba)

    while(len(A)!=0):
        A_i = []
        for i in A:
            for k in B:
                if(k[1]==i or k[2]==i):
                    A_i.append(k[0])
                    B.remove(k)
                    
        ans += len(A)
        A = A_i         
   
    print(ans)

if __name__ == "__main__":
    function()