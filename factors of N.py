N=int(raw_input())
a=[]
for i in range(1,N+1):
    if(N%i==0):
        a.append(i)
print(" ".join(str(i) for i in a))    
