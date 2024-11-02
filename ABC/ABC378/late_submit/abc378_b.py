import math
def function():
    N = int(input())
    q = []
    r = []
    for i in range(N):
        inp_q,inp_r = map(int,input().split())
        q.append(inp_q)
        r.append(inp_r)

    Q = int(input())
    t = []
    d = []
    for i in range(Q):
        inp_t,inp_d = map(int,input().split())
        inp_t -= 1 #添え字調整
        dt = inp_d // q[inp_t]
        da = inp_d - dt*q[inp_t]
        if(da<=r[inp_t]):
            print(q[inp_t]*dt + r[inp_t])
        else:
            print(q[inp_t]*(dt+1) + r[inp_t])
    
    return

if __name__ == "__main__":
    function()