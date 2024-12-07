import numpy

def function():
    N = int(input())
    sqrt_N = int(numpy.sqrt(N))
    A = []
    A = number(sqrt_N)
    
    sum = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if(A[i]*A[j]<= sqrt_N):
                sum +=1
            else:
                break
    for i in range(len(A)):
        if(A[i]**8 <= N):
                sum +=1
        else:
            break
    print(sum)

def number(n):
    li=[int(x) for x in range(3,n+1,2)]
    pri=[2]
    for i in range(n):
        if pri[-1]**2>n:
            pri+=li
            break
        else:
            pri.append(li[0])
            li=[int(x) for x in li if x%pri[-1]!=0]
        if len(li)==0:
            break
    return pri



if __name__ == "__main__":
    function()