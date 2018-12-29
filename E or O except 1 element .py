N=int(raw_input())
a=(raw_input()).split()
a=list(map(int,a))
E=0
O=0
for i in a:
  if(i%2==0):
    E+=1
  else:
    O+=1
if(E>O):
  for i in a:
    if(i%2!=0):
      print(i)
else:
  for i in a:
    if(i%2==0):
      print(i)
