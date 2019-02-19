n,k=map(int,(raw_input()).split())
a=[]
b=[]
for i in range(n):
    a.append(list(map(int,(raw_input()).split())))
for i in range(k):
    if all(a[0][i] in a[j]for j in range(1,n)):
        b=b+[a[0][i]]
b=sorted(b)
print(" ".join(str(i) for i in b))
