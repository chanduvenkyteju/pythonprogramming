N=int(raw_input())
a=(raw_input()).split()
s=0
for i in range(0,(N-1)):
    s+=int(a[i])+int(a[i+1])
print(s)
