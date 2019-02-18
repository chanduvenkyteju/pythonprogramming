n,m=map(int,(raw_input()).split())
a=list(map(int,(raw_input()).split()))
b=list(map(int,(raw_input()).split()))
p=0
q=0
for i in range(0,len(a)):
    p=p+a[i]
    q=q+b[i]
print(q//p)
