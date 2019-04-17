n,k=map(int,(raw_input()).split())
a=list(map(int,(raw_input()).split()))
b=list(map(int,(raw_input()).split()))
c=[]
for i in b:
    a.append(i)
    c.append(max(a))
print(" ".join(str(i) for i in c))
