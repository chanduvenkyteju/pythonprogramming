n=int(raw_input())
a=list(map(int,(raw_input()).split()))
b=[]
for i in range(0,n):
    b.append(a[i])
    if(len(b)<len(a)):
        print(min(b),end=" ")
    else:
        print(min(b))
