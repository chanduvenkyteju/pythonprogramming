a,b=(raw_input()).split()
n=min(len(a),len(b))
s=""
for i in range(n):
    s+=a[i]
    s+=b[i]
k=b if len(b)>len(a) else a
c=1
for i in range(n,len(k)):
    if k==b:
        s+=str(c)
        s+=k[i]
    if k==a:
        s+=k[i]
        s+=str(c)
    c+=1
print(s)
