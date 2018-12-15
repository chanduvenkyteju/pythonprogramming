N=int(raw_input())
a=(raw_input()).split()
b=" ".join(map(str,a))
m=[]
for i in b:
    if(i not in m):
        if(b.count(i)>1):
            m.append(i)
if(len(m)>1):
    n=" ".join(m) 
    h=n[0:1]
    print(h)
else:
    print("unique")
