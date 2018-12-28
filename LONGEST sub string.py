X,Y=map(str,(raw_input()).split())
b=[]
if(Y in X):
    print(Y)
else:
    for i in range(0,len(Y)):
        for j in range(0,len(Y)):
            if(X[i]==Y[j]):
                b.append(X[i])            
print("".join(b))
