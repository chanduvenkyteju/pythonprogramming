S=(raw_input())
c=-1
a=0
if(S[0]>="A" and S[0]<="Z"):
    c=c+1
for i in range(0,len(S)):
    if(S[i]==" "):
        a=a+1
        if(S[i+1]<="Z" and S[i+1]>="A"):
            c=c+1 
if(a==c):
    print("yes")
else:
    print("no")
