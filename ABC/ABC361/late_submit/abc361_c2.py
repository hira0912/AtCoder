def function():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()

    ans = 10**9
    left_key = 0
    right_key = N-K-1
    while(right_key < N):
        if(A[right_key]-A[left_key] < ans):
            ans = A[right_key]-A[left_key]
        left_key += 1
        right_key += 1
    print(ans)
    return

if __name__ == "__main__":
    function()