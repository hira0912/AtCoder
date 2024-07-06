def function():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()

    B = []
    A_bef = A[0]
    for i in range(1,N):
        B.append(A[i]-A_bef)
        A_bef = A[i]
    
    left_key = 0
    right_key = N-1
    for _ in range(K):
        if(B[left_key]>=B[right_key-1]):
            left_key += 1
        else:
            right_key -= 1
    print(A[right_key]-A[left_key])
    return


if __name__ == "__main__":
    function()