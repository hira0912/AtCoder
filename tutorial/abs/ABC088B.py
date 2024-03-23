n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)

sum_a = 0
sum_b = 0

for i in range(n):
    if(i%2==0):
        sum_a += a[i]
    else:
        sum_b += a[i]

print(sum_a - sum_b)
