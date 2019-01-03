N=(raw_input())
a=list(N)
s=0
for i in range(0,len(a)):
    s=s+(int(a[i])**i)
print(s)
