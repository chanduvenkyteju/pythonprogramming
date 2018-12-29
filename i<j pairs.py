N=int(raw_input())
a=(raw_input()).split()
c=0
for i in range(N):
  for j in range(i,N):
    if int(a[i]<a[j]):
      c=c+1
print(c)
