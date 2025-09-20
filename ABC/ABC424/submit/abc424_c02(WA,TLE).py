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
        for b in B:
            for a in A:
                if(b[1]==a or b[2]==a):
                    A_i.append(b[0])
                    B.remove(b)
                    break
                    
        ans += len(A)
        A = A_i         
   
    print(ans)

if __name__ == "__main__":
    function()