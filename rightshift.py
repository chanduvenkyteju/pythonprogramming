K1,N=map(int,input().split())
K=input().split()
while(N>0):
     K.insert(0,K.pop())
     N=N-1
for i in range(0,len(K)):
     if(i!=len(K)-1):
         print(K[i],end=(" "))
     else:
         print(K[i])
