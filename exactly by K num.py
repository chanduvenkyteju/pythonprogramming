S=(raw_input()).split()
K=int(S[2])
S1=S[0]
S2=S[1]
count=0
m=max(len(S1),len(S2))
for i in range(0,m):
        if(S1[i]!=S2[i]):
            count=count+1
        else:
            count=count
if(count==K):
    print("yes")
else:
    print("no")
