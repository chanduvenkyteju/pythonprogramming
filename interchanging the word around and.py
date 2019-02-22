n=(raw_input()).split()
if(len(n)==1):
    print(n[0])
else:
    for i in range(0,len(n)):
        if(n[i]=='and'):
            n[i-1],n[i+1]=n[i+1],n[i-1]
    k=" ".join(map(str,n))
    print(k)
