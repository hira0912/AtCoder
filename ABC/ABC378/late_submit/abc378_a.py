def function():
    A = list(map(int,input().split()))
    sum = 0
    for i in range(1,5):
        sum += A.count(i)//2
    print(sum)
    return

if __name__ == "__main__":
    function()