N=int(raw_input())
c=0
for i in range(0,N+1):
    p=str(i)
    c+=p.count('2')
print(c) 
