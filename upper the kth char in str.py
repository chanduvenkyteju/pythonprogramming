a,b=map(str,(raw_input()).split())
b=int(b)
c=[]
for i in range(0,len(a)):
    if((i+1)%b==0):
        c.append(a[i].capitalize())
    else:
        c.append(a[i])
print("".join(map(str,c)))
