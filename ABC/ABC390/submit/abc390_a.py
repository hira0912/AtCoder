def function():
    A = [1,2,3,4,5]
    B = list(map(int,input().split()))

    if(B[0]==A[1] and B[1]==A[0] and B[2]==A[2] and B[3]==A[3] and B[4]==A[4]):
        print('Yes')
        return
    if(B[0]==A[0] and B[1]==A[2] and B[2]==A[1] and B[3]==A[3] and B[4]==A[4]):
        print('Yes')
        return
    if(B[0]==A[0] and B[1]==A[1] and B[2]==A[3] and B[3]==A[2] and B[4]==A[4]):
        print('Yes')
        return
    if(B[0]==A[0] and B[1]==A[1] and B[2]==A[2] and B[3]==A[4] and B[4]==A[3]):
        print('Yes')
        return
    print('No')

if __name__ == "__main__":
    function()