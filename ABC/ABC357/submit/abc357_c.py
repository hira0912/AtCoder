def function():
    N = int(input())

    arr = []
    arr.append('#')

    def calc(arr):
        narr = []
        karr = ''
        for i in range(len(arr)):
            karr = karr + '.'
        for i in range(len(arr)):
            narr.append(arr[i] + arr[i] + arr[i])
        for i in range(len(arr)):
            narr.append(arr[i] + karr + arr[i])
        for i in range(len(arr)):
            narr.append(arr[i] + arr[i] + arr[i])
        return narr

    for _ in range(N):
        arr = calc(arr)
    
    for i in range(len(arr)):
        print(arr[i])



if __name__ == "__main__":
    function()