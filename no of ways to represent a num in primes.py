n=int(raw_input())
c=0
a=[]
for i in range(2,n):
  x=2
  for x in range(2,i):
    if(i%x==0):
      break
  else:
    a.append(i)
for i in range(0,len(a)):
    j=i
    while(j<len(a)):
        if(a[i]+a[j]==n):
            c=c+1
        j=j+1
print(c)
