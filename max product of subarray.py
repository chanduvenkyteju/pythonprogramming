n = int(raw_input())
a = list(map(int,(raw_input()).split()))
b =[]
for i in range(n):
    c= 1
    for j in range(i,n):
        c= c* a[j]
    b.append(c)
for i in range(n):
    c= 1
    for j in range(i+1):
        c = c* a[j]
    b.append(c)
print(max(b))
