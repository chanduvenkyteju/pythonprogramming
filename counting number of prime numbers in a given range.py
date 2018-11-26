p = int(input( ))
q = int(input( ))
count=0
for n in range(p,q ):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           count=count+1
print(count)  
