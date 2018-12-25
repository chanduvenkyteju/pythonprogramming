N=(raw_input()).split()
N=list(map(int,N))
K=(raw_input()).split()
K=list(map(int,K))
if N[1] not in K:
  K.append(N[1])
K=sorted(K)
m=K.index(N[1])
n=len(K)
if(m==0):
  print(K[1],K[2],K[3],sep=' ')
elif(m==1):
  print(K[0],K[2],K[3],sep=' ')
elif(m==n-1):
  print(K[n-2],K[n-3],K[n-4],sep=' ')
else:
  print(K[m-1],K[m+1],K[m-2],sep=' ')
