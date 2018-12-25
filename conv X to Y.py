X,Y=(raw_input()).split()
X=list(X)
Y=list(Y)
d=len(X)
e=len(Y)
i=0
j=0
c=[]
while d>0:
    if X[i]==Y[j]:
        c.append(X[i])
    j=j+1
    i=i+1
    d=d-1
print(e-len(c))
