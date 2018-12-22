z=1
y=1
x=[]
a=int(raw_input())
p=len(str(a))
y=a
while(a>0):
    z=a%10
    a=a//10
    x.append(z)
for i in range(p-1,-1,-1):
    print(x[i],end=" ")
