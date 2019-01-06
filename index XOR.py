N,Q=map(int,(raw_input()).split())
a=list(map(int,(raw_input()).split()))
k=[]
for i in range(0,Q):
    U,V=map(int,(raw_input()).split())
    s=0
    for j in range(U-1,V):
            s=s^a[j]
    print(s)
