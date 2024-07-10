def function():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())

    for _ in range(Q):
        question = list(map(int,input().split()))
        if(question[0] == 1):
            A[question[1]-1] = question[2]
        else:
            print(A[question[1]-1])
    return

if __name__ == "__main__":
    function()