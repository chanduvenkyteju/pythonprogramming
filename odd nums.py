N=int(raw_input())
a=[]
for i in str(N):
    if(int(i)%2!=0):
        a.append(i)
print(" ".join(a))  
