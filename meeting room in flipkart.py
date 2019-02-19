n=int(raw_input())
a=list(map(eval,(raw_input()).split()))
b=list(map(eval,(raw_input()).split()))
c=1
i=0
while (i<n-1):
  j=i+1
  while(j<n):
    if(b[i]<=a[j]):
      c+=1
      i=j-1
      break
    j+=1
  i+=1
print(str(c))
