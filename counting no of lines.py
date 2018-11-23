x=input()
c=1
for i in range(0,len(x)):
    if(x[i]=="."):
        c=c+1
    else:
        c=c
print(c)
