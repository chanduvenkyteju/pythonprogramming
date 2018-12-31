n=int(raw_input())
l=(raw_input()).split()
l.sort()
c=0
for i in range(n):
    c=c+int(l[i])
if(c!=10):
    print(c)
else:
    print(c-1)
