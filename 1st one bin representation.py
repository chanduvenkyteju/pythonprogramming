a,b=map(int,(raw_input()).split())
c=a*b
d=format(c,"b")
d=d[::-1]
for i in range(0,len(d)):
    if(d[i]=='1'):
        print(i+1)
        break
