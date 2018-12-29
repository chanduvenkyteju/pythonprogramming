N=int(raw_input())
a=(raw_input()).split()
b=[]
for i in range(0,N):
    for j in range(i+1,len(a)):
        if(int(a[i]<a[j])):
            b.append(a[i])
        break
print(b)                   
print(len(b))
         
