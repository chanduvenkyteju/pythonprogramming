l,r=(raw_input()).split()
l=int(l)
r=int(r)
s=0
for i in range(l,r+1):
    if(i%2!=0):
        s=s+i
print(s)
