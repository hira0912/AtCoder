def function():
    N = int(input())
    A = list(map(int,input().split()))
    A_set = set()
    A_set = A
    A = list(A_set)

    A.sort()

    Q = int(input())
    for i in range(Q):
        B = int(input())
        k = (len(A)-1)//2
        kS = 0
        kL = len(A)-1
        while(kS!=kL):
            if(abs(A[k]-B) < abs(A[k+1]-B)):
                kL = k
            else:
                kS = k+1
            k = (kL+kS)//2
        print(abs(A[kL]-B))

if __name__ == "__main__":
    function()