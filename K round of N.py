n,k=map(int,(raw_input()).split())
if n%10==0:
  n=str(n)
  c=0
  for i in range(len(n)-1,-1,-1):
    if(n[i]=='0'):
      c+=1
  if(k<=c):
    print(n)
  else:
    n=n[:-c]
    n=n+'0'*k
    print(n)
elif 10%(n%10)==0:
  p=int('1'+'0'*k)
  while True:
    if(p%n==0):
      print(p)
      break
    else:
      p+=int('1'+'0'*k)
else:
  print(str(n)+k*'0')
