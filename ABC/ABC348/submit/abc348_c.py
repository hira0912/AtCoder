def function():
    N = int(input())
    A = []
    C = []
    for i in range(N):
        a,c = map(int,input().split())
        A.append(a)
        C.append(c)
    
    zip_lists = zip(C,A)
    zip_sort = sorted(zip_lists)
    C,A = zip(*zip_sort)

    data_a = 0
    data_c = 0
    for i in range(N):
        if(C[i]!=data_c):
            data_c = C[i]
            if(A[i] > data_a):
                data_a = A[i]
    print(data_a)

if __name__ == "__main__":
    function()