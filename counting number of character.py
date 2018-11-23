x=input()
c=0
for i in range(0,len(x)):
    if(x[i].isdigit() or x[i].isalpha() or x[i]==" "):
        c=c
    else:
        c=c+1
print(c)
