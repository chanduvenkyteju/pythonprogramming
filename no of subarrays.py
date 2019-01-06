N=int(raw_input())
a=list(map(int,(raw_input()).split()))
s=[]
for i in range(len(a)+1): 
    for j in range(i+1,len(a)+1): 
        s.append(a[i:j]) 
print(len(s)) 
