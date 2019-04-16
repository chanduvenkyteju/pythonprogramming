p,q=map(int,(raw_input()).split())
k=0
l=list(map(int,(raw_input()).split()))
for i in range(0,p):
    for j in range(i,p):
        if(q==l[i]+l[j]):
            k=k+1
if(k>1):
    print("YES")
else:
    print("NO")
