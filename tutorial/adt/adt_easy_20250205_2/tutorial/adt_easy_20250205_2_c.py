from collections import deque

def function():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))

    j = 0
    stock = deque()
    ret = []
    for i in range(1,N+1):
        if(j<M):
            if(i == A[j]):
                stock.append(i)
                j += 1
            else:
                ret.append(i)
                for _ in range(len(stock)):
                    ret.append(stock.pop())
                stock.clear()
        else:
            ret.append(i)
            for _ in range(len(stock)):
                ret.append(stock.pop())
            stock.clear()
    print(*ret)
    return

if __name__ == "__main__":
    function()