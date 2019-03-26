n = int(raw_input())
L = list(map(int,(raw_input()).split()))
K= []
Ldup = []
Lin = []
for i in range(1,n+1) :
    if i not in L :
        K.append(i)
for i in L :
    if L.count(i) > 1 and i not in Ldup :
        Ldup.append(i)
for i in range(0,n) :
    if L[i] in Ldup :
        Lin.append(i)
out = len(K)
for i in range(0,n) :
    if len(K) == 0 :
        break
    if i in Lin :
        if i == Lin[0] :
            if K[0] < L[i] :
                L[i] = K.pop(0)
                Lin.pop(0)
            elif L[i] in Ldup :
                Lin.pop(0)
                Ldup.remove(L[i])
            else :
                L[i] = K.pop(0)
                Lin.pop(0)
print(out)
print(" ".join(str(i) for i in L))
