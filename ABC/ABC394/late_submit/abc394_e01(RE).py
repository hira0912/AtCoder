from collections import deque

def function():
    global N,C
    N = int(input())
    C = []
    for _ in range(N):
        x = []
        ret = str(input())
        for i in range(N):
            x.append(ret[i])
        C.append(x)
    
    for i in range(N):
        ret = []
        for j in range(N):
            ret.append(calc(i,j))
        print(*ret)
    return

def calc(i,j):
    global deq
    deq = deque()
    if(i==j):
        return 0
    getdata(i,j,0,'',-1)
    while(len(deq)):
        print(deq)
        data = deq.popleft()
        exe,result = check(data)
        if(exe==True):
            if(result > 0):
                return result
            elif(C[data[0]][data[1]]!='-'):
                getdata(data[0],data[1],data[2],data[3],data[4])
        if(exe==False):
            getdata(data[0],data[1],data[2],data[3],data[4])
    return -1

def getdata(i,j,k,moj,rireki):
    for m in range(N):
        if(C[i][m] != '-'):
            if(m!=i or m!=rireki):
                data = [m,j,k+1,moj+C[i][m],i]
                deq.append(data)
    return

def check(data):
    if(data[0]==data[1]):
        test = deque()
        for index in range(data[2]):
            test.append(data[3][index])
        flag = 1
        while(len(test)>1):
            if(test.popleft()!=test.pop()):
                flag=0
                break
        if(flag==1):
            return True,data[2]
        return True,-1
    else:
        return False,0

if __name__ == "__main__":
    function()