def function():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()

    def calc(b,k):
        A_new = [abs(x-b) for x in A]
        A_new.sort()
        return(A_new[k-1])

    for _ in range(Q):
        b,k = map(int,input().split())
        print(calc(b,k))
    return

if __name__ == "__main__":
    function()