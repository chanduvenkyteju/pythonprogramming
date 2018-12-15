n=int(raw_input())
a=(raw_input()).split()
b=[]
for i in range(0,len(a)):
    if(int(a[i])==i):
        b.append(i)
if(len(b)!=0):
    s=' '.join(map(str,b))
    print(s)
else:
    print("-1")
