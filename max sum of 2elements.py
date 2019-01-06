N=int(raw_input())
a=(raw_input()).split()
s=0
c=[]
for x in a:
    s=s+int(x)
    c.append(s)
print(max(c))
