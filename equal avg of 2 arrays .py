N=int(raw_input())
a=(raw_input()).split()
b=[]
s=[]
for i in a:
    b.append(int(i))
for i in range(0,len(b)):
    s1=0
    s2=0
    c1=0
    c2=0
    for j in range(i+1,len(b)):
        s1=s1+b[j]
        c1=c1+1
    if(c1>0):
        s1=int(s1/(c1))
    for k in range(0,i+1):
        s2=s2+b[k] 
        c2=c2+1
    if(c2>0):
        s2=int(s2/(c2))
    if(s1==s2):
        print("yes")
        break
else:
    print("no")
