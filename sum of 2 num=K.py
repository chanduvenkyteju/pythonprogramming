def sumpair(N,K,c):
  for i in range(N):
    for j in range(i+1,N):
      if((c[i]+c[j])==K):
        return('yes')
  return('no')
a=(raw_input()).split()
a=list(map(int,a))
b=(raw_input()).split()
b=list(map(int,b))
print(sumpair(a[0],a[1],b))
