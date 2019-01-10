N=int(raw_input())
a=[]
b=[]
for i in range(1,N+1):
    if(N%i==0):
        a.append(i)
for n in a:
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           b.append(n)
print(" ".join(str(i) for i in b)) 
