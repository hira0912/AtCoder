def function():
    H,W = map(int,input().split())
    S = []
    for _ in range(H):
        S.append(str(input()))

    w_min = 9999
    w_max = 0
    h_min = 9999
    h_max = 0

    ## 既存範囲の調査
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                if i < h_min:
                    h_min = i
                if i > h_max:
                    h_max = i
                if j < w_min:
                    w_min = j
                if j > w_max:
                    w_max = j
    
    ## 対象範囲の調査
    for i in range(h_min,h_max+1):
        for j in range(w_min,w_max+1):
            if S[i][j] == '.':
                print('No')
                return
    
    print('Yes')
    return

if __name__ == "__main__":
    function()