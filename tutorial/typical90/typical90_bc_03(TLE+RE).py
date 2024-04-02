import itertools

def function():
    N,P,Q = map(int,input().split())
    A = list(map(int,input().split()))

    if(P==0):
        print(0)
        return

    for i in range(N):
        A[i] = A[i]%P

    count = 0
    A_list = list(itertools.combinations(A,5))
    for j in range(len(A_list)):
        A_list2 = list(A_list[j])
        data = 0
        for k in range(len(A_list2)):
            if(data==0):
                data = A_list2[k]
            else:
                data = (data*A_list2[k])%P
        if(data == Q):
            count += 1
    print(count)

if __name__ == "__main__":
    function()