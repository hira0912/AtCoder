a=int(input())
b=int(input())
c=int(input())
x=int(input())

count = int(0)
for i_a in range(a+1):
    for i_b in range(b+1):
        for i_c in range(c+1):
            if((i_a)*500 + (i_b)*100 + (i_c)*50 == x):count+=1
print(count)