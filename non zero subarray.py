n=int(raw_input())
a=list(map(int,(raw_input()).split()))
n=len(a)
o=[]
for i in range(0,n):
  s=a[i]
  j=i+1
  c=1
  if s<0:
    f=0
    k='n'
  else:
    f=1
    k='p'
  while j<n:
    if f==0 and k=='n' and a[j]>0:
      j+=1
      c+=1
      f=1
      k='p'
    elif f==1 and k=='p' and a[j]<0:
      j+=1
      c+=1
      f=0
      k='n'
    else:
      break
  o.append(c)
print(" ".join(str(i) for i in o))
