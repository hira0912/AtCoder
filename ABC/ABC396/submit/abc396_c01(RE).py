def function():
    N,M = map(int,input().split())
    B = list(map(int,input().split()))
    W = list(map(int,input().split()))

    B.sort(reverse=True)
    W.sort(reverse=True)
    num = 0
    num2 = 0
    total = 0

    for i in range(N):
        if(B[i]<0):
            break
        else:
            total += B[i]
            num += 1

    for j in range(num):
        if(W[j]<0):
            break
        else:
            total += W[j]
            num2 += 1

    j2 = num2
    for i2 in range(num,N):
        if(B[i2]+W[j2] > 0):
            total += B[i2]+W[j2]
            j2 += 1
        else:
            break
    print(total)
    return

if __name__ == "__main__":
    function()