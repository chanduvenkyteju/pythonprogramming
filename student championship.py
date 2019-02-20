n,k=map(eval,(raw_input()).split())
a=list(map(int,(raw_input()).split()))
c=0
s=0
while c<len(a):
  if a[c]+k<=5:
    s=s+1
  c=c+1
print(s//3)
