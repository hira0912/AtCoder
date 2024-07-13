def function():
    # 標準入力
    N = int(input())
    L = []
    R = []
    L_sum = 0
    R_sum = 0

    for _ in range(N):
        data_l, data_r = map(int,input().split())
        L.append(data_l)
        R.append(data_r)
        L_sum += data_l
        R_sum += data_r

    # L,Rの各総和が0を超えていた場合、総和は0にならない
    if(L_sum > 0 or R_sum < 0):
        print('No')
        return
    print('Yes')

    if(abs(L_sum)<=R_sum):
        dist = abs(L_sum)
        mode = 'L'
    else:
        dist = R_sum
        mode = 'R'
    
    X = []
    for i in range(N):
        if(mode == 'L'):
            if(dist == 0):
                X.append(L[i])
            else:
                if((R[i]-L[i])<=dist):
                    X.append(R[i])
                    dist -= (R[i]-L[i])
                else:
                    X.append(L[i]+dist)
                    dist = 0
        else:
            if(dist == 0):
                X.append(R[i])
            else:
                if((R[i]-L[i])<=dist):
                    X.append(L[i])
                    dist -= (R[i]-L[i])
                else:
                    X.append(R[i]-dist)
                    dist = 0            
    print(*X)
    return

if __name__ == "__main__":
    function()