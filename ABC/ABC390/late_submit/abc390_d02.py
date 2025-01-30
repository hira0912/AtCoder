def function():
    global N,A,S,B
    # input
    N = int(input())
    A = list(map(int,input().split()))
    # global variables
    S = [0]*12
    B = set()
    # calculation
    calc(0,0)
    print(len(B))
    return

def calc(index:int, size:int) -> None:
    # index over
    if(index>=N):
        B.add(xor(S))
        return
    
    # dfs
    for i in range(size+1):
        S[i] += A[index]
        if(i<size):
            calc(index+1,size)
        else:
            calc(index+1,size+1)
        S[i] -= A[index]           

# calculate xor
def xor(A:list)->int:
    ret = A[0]
    for i in range(1,len(A)):
        ret = ret^A[i]
    return ret

if __name__ == "__main__":
    function()