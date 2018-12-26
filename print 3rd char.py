S=str(raw_input())
k=[]
for i in range(0,len(S),3):
    k.append(S[i])
S=''.join(map(str,k))
print(S)
