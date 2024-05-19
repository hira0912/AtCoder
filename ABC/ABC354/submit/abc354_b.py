def function():
    N = int(input())
    data = []
    sum = 0
    for i in range(N):
        data.append(list(map(str,input().split())))
        sum += int(data[i][1])

    data.sort()
    print(data[sum%N][0])

if __name__ == "__main__":
    function()