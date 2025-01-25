def function():
    N = int(input())
    A = list(map(int,input().split()))

    B = set()
    B.add(xor(A))
    B.union(calc(A,B))
    print(len(B))
    return

def calc(A:list,B:set)->set:
    if(len(A)<2):
        B.add(xor(A))
        return B
    B.add(xor(A))
    for i in range(len(A)):
        for j in range(len(A)):
            if(i!=j):
                A_dup = list(A)
                A_dup[i] += A_dup[j]
                del A_dup[j]
                B.add(xor(A))
                if(len(A)>=2):
                    B.union(calc(A_dup,B))
    return B

def xor(A:list)->int:
    ret = A[0]
    for i in range(1,len(A)):
        ret = ret^A[i]
    return ret

if __name__ == "__main__":
    function()