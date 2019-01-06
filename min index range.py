N,Q=map(int,(raw_input()).split())
l=list(map(int,(raw_input()).split()))
k=[]
for i in range(0,Q):
    U,V=map(int,(raw_input()).split())
    s=0
    m=l[U-1]
    for j in range(U-1,V):
        if(l[j]<m):
            m=l[j]
    print(m)
