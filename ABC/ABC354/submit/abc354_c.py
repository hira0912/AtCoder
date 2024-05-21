def function():
    # 標準入力と配列格納
    m = int(input())
    data = []
    for i in range(m):
        k = list(map(int,input().split()))
        k.append(i+1)
        data.append(k)
    
    # 逆順ソート
    data.sort(reverse=True)

    # 配列dataの読み込み、条件OKの要素だけ配列番号を配列xに書き出す
    x = []
    count = 0
    i = 0
    i_data = 0
    while count < m:
        if(i==0):
            x.append(data[i][2])
            i_data = data[i][1]
            i += 1
        else:
            if(data[i][1] > i_data):
                i += 1
            else:
                x.append(data[i][2])
                i_data = data[i][1]
                i += 1
        count += 1

    # 配列xを昇順ソート
    x.sort()
    
    # 配列xの長さと要素を出力
    print(len(x))
    print(*x)

if __name__ == "__main__":
    function()