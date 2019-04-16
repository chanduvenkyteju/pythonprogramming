n,m=map(eval,(raw_input()).split())
a=[]
for k in range(n):
  a.append(list(map(eval,(raw_input()).split())))
p=[]
arr=[]
temp=[]
t=[]
i=0
j=0
arr.append(a[i][j])
p.append([i,j])
while [n-1,m-1] not in p:
  i=0
  for k in p:
    if k[0]+1<n and k[1]+1<m:
      temp.append(a[k[0]+1][k[1]]+arr[i])
      temp.append(a[k[0]][k[1]+1]+arr[i])
      t.append([k[0]+1,k[1]])
      t.append([k[0],k[1]+1])
    elif k[0]+1<n:
      temp.append(a[k[0]+1][k[1]]+arr[i])
      t.append([k[0]+1,k[1]])
    elif k[1]+1<m:
      temp.append(a[k[0]][k[1]+1]+arr[i])
      t.append([k[0],k[1]+1])
    i+=1
  p=t
  t=[]
  arr=temp
  temp=[]
print(max(arr))
