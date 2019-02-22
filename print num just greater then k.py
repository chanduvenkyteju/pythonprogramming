m,n=map(int,(raw_input()).split())
a=(raw_input()).split()
b=[]
for i in a:
    b.append(int(i))
b.sort()
for i in range(0,len(b)):
    if(b[i]>n):
        print(b[i])
        break
