from collections import deque

def function():
    A = deque()
    for _ in range(100):
        A.append(0)

    Q = int(input())
    for i in range(Q):
        data = list(map(int,input().split()))
        if(data[0]==2):
            print(A.pop())
        else:
            A.append(int(data[1]))
    return

if __name__ == "__main__":
    function()