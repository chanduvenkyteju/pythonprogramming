k,m=map(int,(raw_input()).split())
E=[]
for j in range(m):
  E.append(list(map(int,(raw_input()).split())))
maxi=0
for i in range(m):
  if E[i][0]==1:
    q=1
    q+=E[i][1]
    s=E[i][1]
    j=i+1
    while j<m:
      if E[j][0]==s:
        q+=E[j][1]
        s=E[j][1]
      j+=1
  if q>maxi:
    maxi=q
print(maxi)
