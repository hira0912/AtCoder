import bisect

def function():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A.sort()
    B.sort()

    ans = 1111111111
    for i in range(N):
        k = bisect.bisect_left(B,A[i])
        if(k==0):
            if(ans > abs(A[i]-B[k])):
                ans = abs(A[i]-B[k])  
        else:
            if(ans > abs(A[i]-B[k])):
                ans = abs(A[i]-B[k])    
            elif(ans < abs(A[i]-B[k+1])):            



if __name__ == "__main__":
    function()