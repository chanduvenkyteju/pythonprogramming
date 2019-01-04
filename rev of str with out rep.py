S=str(raw_input())
p=[]
for i in S:
    if(i not in p):
        p.append(i)
p=p[::-1]
K="".join(map(str,p))
print(K)
