def function():
    S = str(input())
    K = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    pos = 0
    # 初期posの設定
    for i in range(len(S)):
        if(S[i]=='A'):
            pos = i
            break

    total = 0
    # 移動距離計算
    for i in range(1,len(K)):
        for j in range(len(S)):
            if(S[j]==K[i]):
                total += abs(pos-j)
                pos = j
                break
    print(total)
    return

if __name__ == "__main__":
    function()