n,a,b = map(int,input().split())

count = int(0)
for i in range(n+1):
    
    # n = 0の時は除外
    if(i==0):
        continue
    
    i_str = str(i)
    i_list_int = map(int,i_str)
    i_sum = sum(i_list_int)
    if(i_sum >= a and i_sum <= b):
        count += i

print(count)