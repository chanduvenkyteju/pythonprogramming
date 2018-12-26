N,K=(raw_input().split())
N=int(N)
K=int(K)
c=0
b=[]
a=(raw_input()).split()
for i in a:
    if(a.count(i)==K):
        b.append(i)
        while i in a:
            a.remove(i)
print("".join(b))
