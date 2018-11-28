N=int(input())
a=[]
S='kabali'
for i in range(0,N):
    a.append(str(input()))
count=0
for i in range(0,N):
    if(sorted(a[i])==sorted(S)):
        count=count+1
    else:
        count=count
print(count) 
