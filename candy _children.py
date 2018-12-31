n=int(raaw_input())
l=(raw_input()).split()
l.sort()
c=0
for i in range(n):
    c=c+int(l[i])
print(c)
