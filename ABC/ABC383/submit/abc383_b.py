def function():
    H,W,D = map(int,input().split())
    A = []
    for _ in range(H):
        A.append(str(input()))
    
    B1 = []
    B2 = []
    for i in range(H):
        for j in range(W):
            if A[i][j]=='.':
                B1.append(i)
                B2.append(j)

    max = 0
    for i in range(len(B1)):
        for j in range(i+1,len(B1)):
            value = calc(A,B1[i],B2[i],B1[j],B2[j],H,W,D)
            if(value>max):
                max = value
    print(max)
    return

def calc(map,B1,B2,C1,C2,H,W,D):
    ret = 0
    for i in range(H):
        for j in range(W):
            if(map[i][j]=='.'):
                if((abs(i-B1)+abs(j-B2)<=D)or(abs(i-C1)+abs(j-C2)<=D)):
                    ret += 1
    return ret



if __name__ == "__main__":
    function()