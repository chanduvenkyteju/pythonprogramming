a,b=map(eval,(raw_input()).split())
k=[]
for i in range(a):
  k.append(list(map(eval,(raw_input()).split())))
for i in range(len(k)):
  for j in range(len(k[i])):
    if k[i][j]==0:
      for i2 in range(a):
        if k[i2][j]!=0:
          k[i2][j]=9
      for j2 in range(b):
        if k[i][j2]!=0:
          k[i][j2]=9
for i in range(len(k)):
  for j in range(len(k[i])):
    if k[i][j]==9:
      k[i][j]=0
  print(" ".join(str(i) for i in k[i]))
