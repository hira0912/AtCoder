def function():
    N = int(input())
    A = list(map(int,input().split()))
    A_set = set()
    A_set = A
    A_set.sort()
    A = list(A_set)
    Q = int(input())

    A_len = len(A)

    for _ in range(Q):
        B = int(input())
        a=0
        b=A_len-1
        while(a<=b):
            c = (a+b)//2
            if(A[c]>=B):
                b = c-1
            else:
                a = c+1
        if(a==0):
            abst = abs(A[a]-B)
        elif(a==A_len):
            abst = abs(A[a-1]-B)
        else:
            if abs(A[a]-B)>abs(A[a-1]-B):
                abst = abs(A[a-1]-B)
            else:
                abst = abs(A[a]-B)
        print(abst)

if __name__ == "__main__":
    function()