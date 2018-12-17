a,b=(raw_input().split( ))
a=int(a)
b=int(b)
p=[]
c=0
for i in range(a,b+1):
    m=list(bin(i))
    del m[1]
    m=map(int,m)
    p.append(sum(m))
for i in p:
    if i>1:
       for j in range(2,i):
           if i%j==0:
               break
       else:
            c+=1
print(c)
