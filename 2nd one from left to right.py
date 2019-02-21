a,b=map(int,(raw_input()).split())
c=a*b
d=format(c,"b")
k=[]
for i in range(0,len(d)):
    if(d[i]=='1'):
        k.append(i)
print(max(k)+1)
