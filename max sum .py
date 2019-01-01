N=int(raw_input())
a=[]
a=list(map(int,(raw_input()).split()))
a1=a[::2]
a2=a[1::2]
a3=a[1::3]
if(sum(a1)>sum(a2) and sum(a1)>sum(a3)):
  print(sum(a1))
elif(sum(a3)>sum(a1) and sum(a3)>sum(a2)):
  print(sum(a3))
else:
    print(sum(a2))
