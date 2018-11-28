N=int(input())
a=[]
for i in range(0,N):
    a.append(str(input()))
c=0
S="kabali"
for i in range(0,N):
    if(sorted(a[i])==sorted(S)):
        c=c+1
    else:
        c=c
print(c) 
