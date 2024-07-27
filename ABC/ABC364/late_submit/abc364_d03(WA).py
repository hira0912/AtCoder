import bisect

def function():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()

    def calc(b,k):
        def check(x):
            lb = bisect.bisect_left(A,b-x)
            ub = bisect.bisect_right(A,b+x)
            if(ub-lb>=k):
                return False
            else:
                return True
    
        ok = 10**8 + 1
        ng = -1
        ans = 0
        while(ok-ng>1):
            mid = (ok+ng)//2
            if(check(mid)==False):
                ok = mid
            else:
                ng = mid
        return ok

    for _ in range(Q):
        b,k = map(int,input().split())
        print(calc(b,k))
    return

if __name__ == "__main__":
    function()