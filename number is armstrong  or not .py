z = int(input( ))
y =0
t = num
while t > 0:
   d = t % 10
   y += d ** 3
   t //= 10
if z == y:
   print("yes")
else:
   print(" no")
