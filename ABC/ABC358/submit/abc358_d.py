def function():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()

    ans = 0
    left = 0
    leng = len(A)
    for i in range(len(B)):
        while True:
            if(left == leng):
                print('-1')
                return
            if(B[i] > A[left]):
                left += 1
            else:
                ans += A[left]
                left += 1
                break
    print(ans)

if __name__ == "__main__":
    function()