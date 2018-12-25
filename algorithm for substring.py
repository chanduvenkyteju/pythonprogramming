A,B=(raw_input()).split()
for i in range(len(A)):
   if(i<len(A)-1): 
      if(A[i]+A[i+1] in B):
         print("yes")
         break
else:
    print("no")
