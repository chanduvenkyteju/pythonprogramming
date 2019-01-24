N=int(raw_input())
a=[]
for i in range(0,N):
    a.append((raw_input()))
for j in range(0,len(a)):
    for k in range(j+1,len(a)):
        if(a[j]==a[k]):
            print("yes")
else:
    print("no")
