S1,S2=map(str,(raw_input()).split())
K=int(raw_input())
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
