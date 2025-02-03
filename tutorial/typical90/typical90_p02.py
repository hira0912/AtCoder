def function():
    global N,A
    N = int(input())
    A = []
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    x = N // A[0]
    ret = calc(x,0,0)
    print(ret)

def calc(x,y,z):
    val = 10000
    for i in range(x,-1,-1):
        y = (N-i*A[0]) // A[1]
        for j in range(y,-1,-1):
            z = (N-i*A[0]-j*A[1]) // A[2]
            ret = i*A[0]+j*A[1]+z*A[2]
            if(ret==N):
                if(val > i+j+z):
                    val = i+j+z
                break
    return val
            
if __name__ == "__main__":
    function()