N=int(raw_input())
a=(raw_input()).split()
b=[]
for i in a:
    b.append(int(i))
c=(b.index(min(b))+1)
d=(b.index(max(b))+1)
print(c,d)
