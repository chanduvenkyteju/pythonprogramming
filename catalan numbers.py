def fact(l):
    k=1
    for i in range(1,l+1):
        k=k*i
    return m

n=int(raw_input())
a=[]
i=0
while(i<=n):
    if(i==0):
        a.append(1)
    else:
        a.append(fact(2*i)//((fact(i+1))*fact(i)))
    i=i+1
p=" ".join((str(i)for i in a))
print(p)
