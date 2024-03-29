n = int(input())

x_p,y_p,t_p = 0,0,0
result = "Yes"
for i in range(n):
   t,x,y = map(int,input().split())
   if(abs(t-t_p) < abs(x-x_p)+abs(y-y_p) or abs(t-t_p)%2 != (abs(x-x_p)+abs(y-y_p))%2):
       result = "No"
       break
   t_p,x_p,y_p = t,x,y

print(result)
