x =int(input())
m = 1
n = 1
c = 0
if x<= 0:
   print(" enter a positive integer")
elif x == 1:
   print(m)
else:
   while c < x:
       print(m,end=' , ')
       y = m + n
       m = n
       n = y
       c += 1
