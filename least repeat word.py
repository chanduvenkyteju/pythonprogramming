S=(raw_input())
T=str(S.lower())
M=[]
for i in T:
    if(T.count(i)==1):
        M.append(i)
St=" ".join(map(str,M))
print(St)
