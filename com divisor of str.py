m=(raw_input())
n=(raw_input())
import sys
if len(m)>len(n):
  print(1)
  sys.exit(0)
a=[]
s=''
for i in range(len(m)):
  if m[i] not in a:
    s+=m[i]
    a.append(m[i])
k=0
k=len(m)//len(s)
q=1
for i in range(2,k+1):
  if k%i==0:
    q+=1
print(q)
