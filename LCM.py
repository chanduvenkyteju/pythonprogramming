N,M=map(int,(raw_input()).split())
for x in range(1,(N*M)+1):
    if(x%N==0 and x%M==0):
      print(x)
      break
