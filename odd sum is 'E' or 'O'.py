N=str(raw_input())
a=[]
c=0
for i in (N):
    if(int(i)%2!=0):
        a.append(i)
#print(a)        
for j in a:
    c=c+int(j)
#print(c)    
if(c%2==0):
    print("E")
else:
    print("O")
