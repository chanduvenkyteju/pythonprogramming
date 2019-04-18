N=int(raw_input())
a=list(map(int,(raw_input()).split()))
b=[]
for i in a:
    if(i<0):
        b.append(i)
c=sum(b)
print(c)
