n=int(input())
a,b=[],[]
c=0
for i in range(0,n):
  a.append(list(map(int,input().split())))
for i in range(0,n+2):
  if i==0:
    b.append([0]*(n+2))
  elif i==(n+2)-1:
    b.append([0]*(n+2))
  else:
    b.append([0]+a[i-1]+[0])
for i in range(0,len(b)):
    for j in range(0,len(b)):
      if b[i][j]!=0 and n%2==0:
        if b[i-1][j-1]==0 and b[i-1][j]==0 and b[i-1][j+1]==0 and b[i][j-1]==0 and b[i][j+1]==0 and b[i+1][j-1]==0 and b[i+1][j]==0 and b[i+1][j-1]==0:
            c+=1
      elif b[i][j]!=0 and n%2!=0:
        if b[i][j-1]==0 and b[i][j+1]==0 and b[i-1][j]==0 and b[i+1][j]==0:
            c+=1
print(c)
