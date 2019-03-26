n=int(raw_input())
k=list(map(int,(raw_input()).split()))
s=[]
for i in range(0,n-1):
  if k[i]>max(k[i+1:]):
    s.append(k[i])
s.append(k[n-1])
print(" ".join(str(i) for i in s))
print(max(k))
