X,Y=(raw_input()).split()
X=list(X)
Y=list(Y)
p=abs(len(X)-len(Y))
n=len(min(X,Y))
for i in range(n):
    if X[i]!=Y[i]:
        p=p+1
print(p)
