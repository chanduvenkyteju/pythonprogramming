a,b=map(int,(raw_input()).split())
m=0
x=b-1
while(m==0 and x>1):
    if(b%x==0 and a%x==0):
        m+=1
    x-=1
print(x+1)
