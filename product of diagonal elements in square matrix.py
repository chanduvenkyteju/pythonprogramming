n=int(raw_input())
l=[]
k=1
s=1
for i in range(n):
    l.append(list(map(int,(raw_input()).split())))
for i in range(n):
    k=k*l[i][i]
for j in range(n):
    s=s*l[j][n-j-1]
print(s+k)
