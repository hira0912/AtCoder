def function():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()

    def calc(b,k):
        if(b<A[0]):
            ok = 0
        elif(b>A[N-1]):
            ok = N
        else:
            ok = N
            ng = -1
            while(abs(ok-ng)>1):
                mid = (ok+ng)//2
                if(A[mid] >= b):
                    ok = mid
                else:
                    ng = mid
    
        left = ok
        right = ok
        k_count = 0
        ans = 0

        while(k_count<k):
            if(left<=0):
                right += 1
                ans = abs(A[right-1]-b)
            elif(right>=N):
                left -= 1
                ans = abs(A[left]-b) 
            else:
                if(abs(A[left-1]-b)<abs(A[right]-b)):
                    left -= 1
                    ans = abs(A[left]-b) 
                else:
                    right += 1
                    ans = abs(A[right-1]-b)                  
            k_count += 1
        return ans

    for _ in range(Q):
        b,k = map(int,input().split())
        print(calc(b,k))
    return

if __name__ == "__main__":
    function()