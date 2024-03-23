d = int(input())
data = list(map(int,input().split()))

flag = int(0)
count = int(0)
while(flag==0):
    for i in range(d):
        if(data[i] %2 != 0):
            flag=1
            break
    if(flag==0):
        count += 1
        for i in range(d):
            data[i] = data[i] /2
print(count)