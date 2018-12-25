N=list(map(int,(raw_input()).split()))
b=sorted(list(map(int,(raw_input()).split())))[::-1]
S=0
for i in range(len(b)):
  if(N[1]>=b[i]):
    S+=int(N[1]/b[i])
    N[1]%=b[i]
if(N[1]==0):
  print(S)
else:
  print("not possible")
