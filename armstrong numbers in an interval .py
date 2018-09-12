x=int(input())
y=int(input())
for n in range(x,y):
    p= len(str(n))
    s = 0
    t = n
    while t > 0:
       d = t % 10
       s+= d ** p
       t //= 10
    if n == s:
       print(n,end=" ")
