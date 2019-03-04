a=(raw_input())
n=''
for i in range(0,len(a)-1,2):
  if int(a[i+1])%2==0:
    n+=a[i]*int(a[i+1])
  else:
    n+=a[i]+a[i+1]
print(n)
