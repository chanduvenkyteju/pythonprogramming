def fun(s,z):
    l=z+1
    if l==len(s):
        return 1
    else:
        if s[z]=='a' and s[l]=='b':
            return 1+fun(s,l)
        if s[z]=='b' and s[l]=='a':
            return 1+fun(s,l)
        else:
            return 1
n=(raw_input())
t=[]
for z in range(len(n)-1):
    if n[z]=='a' and n[z+1]=='b':
        t.append(fun(n,z))
if len(t)==0:
    print(0)
else:
    print(max(t))
