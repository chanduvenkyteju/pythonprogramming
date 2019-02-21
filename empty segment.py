n,k=map(int,(raw_input()).split())
a= []
(p,q) = ([],[])
a = list(map(int,(raw_input()).split()))
if(n%2!=0):
    p=a[:n-1]
    q=a[n-1:n]
else:
    p=a[:n//2]
    q=a[n//2:n]
print(max(min(p),min(q)))
