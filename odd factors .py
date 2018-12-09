N=int(raw_input())
a=[]
for i in range(1,N+1):
    if(N%i==0 and i%2!=0):
        a.append(i)
s=" ".join(map(str,a))
print(s)
