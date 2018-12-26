N,K=map(int,(raw_input()).split())
a=input().split()
for i in range(0,N):
    if(int(a[i])==K):
        print("Yes")
        break
    else:
        print("No")
