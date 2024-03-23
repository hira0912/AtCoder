n,y = map(int,input().split())
y = int(y/1000)

a_10000,a_5000,a_1000 = -1,-1,-1
for i_10000 in reversed(range(n+1)):
    for i_5000 in reversed(range(n+1-i_10000)):
        i_1000 = n - i_5000 - i_10000
        money = i_10000*10 + i_5000*5 + i_1000*1
        if(money == y):
            a_10000,a_5000,a_1000 = i_10000,i_5000,i_1000
            break
    else:continue
    break

print(a_10000,a_5000,a_1000)