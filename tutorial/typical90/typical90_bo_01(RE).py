def function():
    N,K = map(int,input().split())
    data = N
    for i in range(K):
        data = change_8_9(data)
    print(data)
    return

def change_8_9(data):
    data = change_n_10(data,8)
    data = change_10_n(data,9)
    data = int(str(data).replace('8','5'))
    return data

def change_n_10(data,n):
    data_10 = 0
    for s in str(data):
        data_10 *= n
        data_10 += int(s)
    return data_10

def change_10_n(data,n):
    ret = ""
    while data:
        ret += str(data % n)
        data //= n
    return str(ret[::-1])

if __name__ == "__main__":
    function()