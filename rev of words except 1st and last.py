S=(raw_input().split())
a=[]
for i in range(0,len(S)):
    if(i==0 or i==len(S)-1):
        a.append(S[i])
    else:    
        a.append(S[i][::-1])
K=" ".join(a)
print(K)
