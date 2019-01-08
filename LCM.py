N,M=map(int,(raw_input()).split())
for i in range(1,(N*M)+1):
    if(i%N==0 and i%M==0):
      print(i)
      break
