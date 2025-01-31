def function():
    N = int(input())
    A = list(map(int,input().split()))
    A_set = set()
    A_set = A
    A_set.sort()
    A = list(A_set)
    Q = int(input())

    A_len = len(A)

    for _ in range(Q):
        B = int(input())
        left=0
        right=A_len-1
        while(left<=right):
            mid = (left+right)//2
            if(A[mid]>=B):
                right = mid-1
            else:
                left = mid+1
        if(left==0):
            abst = abs(A[left]-B)
        elif(left==A_len):
            abst = abs(A[left-1]-B)
        else:
            if abs(A[left]-B)>abs(A[left-1]-B):
                abst = abs(A[left-1]-B)
            else:
                abst = abs(A[left]-B)
        print(abst)

if __name__ == "__main__":
    function()