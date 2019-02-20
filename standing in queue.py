n=int(raw_input())
a=sorted(list(map(int,(raw_input()).split())))
c=1
for i in range(1,n):
  if sum(a[:i])<=a[i]:
    c+=1
print(c)
