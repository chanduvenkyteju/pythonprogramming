n=int(raw_input())
l=list(map(int,(raw_input()).split()))
a=[]
for i in l:
    if(i!=0):
        a.append(i)
while(len(a)!=n):
    a.append(0)
print(" ".join(map(str,a)))
