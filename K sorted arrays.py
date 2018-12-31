m=[]
n=[]
K=int(raw_input())
for i in range(K):
    n.append(raw_input().split())
for j in n:
    for y in j:
        m.append(int(y))
m.sort()
s=" ".join(map(str,m))
print(s)
