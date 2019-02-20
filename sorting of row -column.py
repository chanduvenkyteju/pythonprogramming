p,q=map(int,(raw_input()).split())
if p<=q:
  d=p
else:
  d=q
a=[]
for i in range(0,d):
  a.append(sorted(list(map(int,(raw_input()).split()))))
a=sorted(a)
for i in range(0,len(a[0])):
  for j in range(0,len(a)-1):
    if a[j][i]>a[j+1][i]:
      a[j][i],a[j+1][i]=a[j+1][i],a[j][i]
for i in a:
  print(*i)
