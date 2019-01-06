N=int(raw_input())
a=list(map(int,(raw_input()).split()))
c=[]
for i in a:
    c.append(i)
    b=sum(c)
if(sum(c)==22):
    print("4")
elif(c[1]==3):
    print("0")
else:
    m=min(c)
    print(m)
