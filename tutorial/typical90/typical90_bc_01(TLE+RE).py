import itertools,math

def function():
    N,P,Q = map(int,input().split())
    A = list(map(int,input().split()))

    for i in range(N):
        A[i] = A[i]%P

    count = 0
    A_list = list(itertools.combinations(A,5))
    for j in range(len(A_list)):
        A_list2 = list(A_list[j])
        if((math.prod(A_list2)-Q)%P == 0):
            count += 1
    print(count)

if __name__ == "__main__":
    function()