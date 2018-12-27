N=(raw_input()).split()
N=list(Nap(int,N))
n=N[0]/2
a=N[1]
b=N[2]
d=int(N[0]/a)
e=int(N[0]/b)
c=0
if(N[0]%2==0):
  for i in range(1,d):
    for j in range(1,e):
      if((a*i)+(b*j)==n):
        c=1
if(c==1):
  print('YES')
else:
  print('NO')
