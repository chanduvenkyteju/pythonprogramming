z=str(input())
p=0
for i in range(0,len(z)):
    if(z[i]=='('):
        p=p+1
    if(z[i]==')'):
        p=p-1
if(p==0):
    print("yes")
else:
    print("no")
