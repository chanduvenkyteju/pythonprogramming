X,Y=(raw_input()).split()
X=list(X)
Y=list(Y)
p=abs(len(X)-len(Y))
n=len(max(X,Y))
for i in range(n-1):
    if X[i]!=Y[i]:
        p=p+1
print(p)
