N=int(raw_input())
K=bin(N)[2:]
a=[]
L=K[::-1]
for i in range(0,len(L)):
    if(L[i]=='1'):
        a.append(i)
print(min(a)+1)
