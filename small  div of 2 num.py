L,R=map(int,input().split())
if(L>R):
    c=L
else:
    c=R
while(True):
    if((c%L==0) and (c%R==0)):
        l=c
        break
    c+=1
print(l) 
