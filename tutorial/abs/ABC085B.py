n = int(input())
d = []
for i in range(n):
    d.append(int(input()))

d.sort()
flag=0
while(flag==0):
    flag=1
    for i in range(len(d)):
        if(i==0):continue
        if(d[i]==d[i-1]):
            del d[i]
            flag=0
            break

print(len(d))