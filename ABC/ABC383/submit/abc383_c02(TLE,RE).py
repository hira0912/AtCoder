def function():
    H,W,D = map(int,input().split())
    A = []
    for _ in range(H):
        A.append(str(input()))
    
    H1 = []
    H2 = []
    for i in range(H):
        for j in range(W):
            if A[i][j]=='H':
                H1.append(i)
                H2.append(j)

    for k in range(len(H1)):
        A = calc(A,H1[k],H2[k],H,W,D)

    sum = 0
    for i in range(H):
        for j in range(W):
            if(A[i][j]=='@' or A[i][j]=='H'):
                sum+=1
    print(sum)
    return

def calc(map:list,B1,B2,H,W,D)->list:
    if(D==0):
        return map
    
    vector = [[1,0],[-1,0],[0,1],[0,-1]]
    for c in vector:
        if(B1+c[0]<0 or B1+c[0]>H-1 or B2+c[1]<0 or B2+c[1]>W-1):
            continue
        if(map[B1+c[0]][B2+c[1]]=='H' or map[B1+c[0]][B2+c[1]]=='#'):
            continue
        map[B1+c[0]] = map[B1+c[0]][:(B2+c[1])] + '@' + map[B1+c[0]][(B2+c[1]+1):]
        map = calc(map,B1+c[0],B2+c[1],H,W,D-1)
    return map

if __name__ == "__main__":
    function()