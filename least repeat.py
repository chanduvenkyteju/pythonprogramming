S=(raw_input())
s=str(S.lower())
p=[]
for i in s:
    if(s.count(i)==1):
        p.append(i)
St=" ".join(map(str,p))
print(St)
