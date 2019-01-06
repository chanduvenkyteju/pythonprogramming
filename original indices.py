N=int(raw_input())
a=list(map(int,(raw_input()).split()))
b=sorted(a)
c=[]
for i in b :
    c.append(a.index(i)+1)
print(" ".join(str(i) for i in c))
