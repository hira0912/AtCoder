def function():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))       

    ans1 = 0
    for i in range(N):
        if(A[i]==B[i]):
            ans1 += 1
    print(ans1)

    ans2 = 0
    A.sort()
    B.sort()

    i = 0
    j = 0
    while(True):
        if(i==N or j==N):
            break
        if(A[i]==B[j]):
            ans2 += 1
            i += 1
            j += 1
        elif(A[i]>B[j]):
            j += 1
        elif(A[i]<B[j]):
            i += 1
    print(ans2-ans1)
    return

if __name__ == "__main__":
    function()