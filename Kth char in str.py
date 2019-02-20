S,K=map(str,(raw_input()).split())
K=int(K)
a=[]
for i in range(K-1,len(S),K):
    a.append(S[i])
print(" ".join(map(str,a)))
