n=int(input())
a=[]
for i in range(1,n+1):
    a.append(int(input()))
    ind=a.index(i)
for i in range(0,n):
    print(i,ind)
