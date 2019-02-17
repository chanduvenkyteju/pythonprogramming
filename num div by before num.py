N=int(raw_input())
a=list(map(int,input().split()))
b=[]
for i in range(1,len(a)):
    if(a[i]%a[i-1]==0):
        b.append(a[i])
print(" ".join(str(i) for i in b))        
