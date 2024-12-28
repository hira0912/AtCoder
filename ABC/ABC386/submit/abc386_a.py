def function():
    A = []
    a1,a2,a3,a4 = map(int,input().split())
    A.append(a1)
    A.append(a2)
    A.append(a3)
    A.append(a4)
    A.sort()

    ret = 'No'
    if(A[0]==A[1]) and (A[1]==A[2]):
        ret = 'Yes'
    if(A[1]==A[2]) and (A[2]==A[3]):
        ret = 'Yes'
    if(A[0]==A[1]) and (A[2]==A[3]):
        ret = 'Yes'
    if(A[0]==A[1]) and (A[1]==A[2]) and (A[2]==A[3]):
        ret = 'No'
    print(ret)

if __name__ == "__main__":
    function()