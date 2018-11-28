N=int(input())
a=[]
for i in range(0,N):
    a.append(int(input()))
for j in range(0,len(a)):
    for k in range(0,len(a)):
        if(a[j]!=a[k]):
            break
print(a[j])
