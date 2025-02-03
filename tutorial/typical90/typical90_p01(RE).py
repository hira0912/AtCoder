def function():
    global N,A
    N = int(input())
    A = []
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    x = N // A[0]
    y = (N-x*A[0]) // A[1]
    z = (N-x*A[0]-y*A[1]) // A[2]
    ret = dfs(x,y,z)
    print(ret)

def dfs(x,y,z):
    ret = x*A[0] + y*A[1] + z*A[2]
    if(ret==N):
        return x+y+z
    else:
        x -= 1
        y = (N-x*A[0]) // A[1]
        z = (N-x*A[0]-y*A[1]) // A[2]
        ret = dfs(x,y,z)
    return ret
            
if __name__ == "__main__":
    function()