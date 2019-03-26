m=int(raw_input())
n=list(map(int,(raw_input()).split()))
for i in range(0,m):
    if(n[i]==min(n)):
        c=i 
        break
for i in range(0,m):
    if(n[i]==max(n)):
        d=i 
        break
print(abs(c-d))
