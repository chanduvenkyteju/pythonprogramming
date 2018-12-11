S,K=map(str,(raw_input()).split())
c=1
for i in S:
    if(K==i):
        print(c)
        break
    else:
        c=c+1
