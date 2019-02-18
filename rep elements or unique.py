n=int(raw_input())
a=list(map(int,(raw_input()).split()))
a.sort()
b=[]
for i in range(0,n-1):
  if(a[i]==a[i+1]):
    if(a[i] not in b):
      b.append(a[i])
b.sort()
if len(b)!=0:
  print(" ".join(str(i) for i in b))
elif len(b)==0:
  print("unique")
