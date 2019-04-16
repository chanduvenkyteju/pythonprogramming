def dhoni(n):
  i=0
  while(i<(n+int(n/2))):
    k=2
    while(k<=n):
      if(i+1==(n+int(n/2))):
        print(k)
        return
      else:
        print(k,end=' ')
        k+=2
        i+=1
    k=1
    while(k<=n):
      if(i+1==(n+int(n/2))):
        print(k)
        return
      else:
        print(k,end=' ')
        k+=2
        i+=1    
n=int(raw_input())
print(n+int(n/2))
dhoni(n)
