n=int(raw_input())
c=0
for i in range(0,len(n)):
    for j in range(0,i+1):
        c=c+int(n[j])
print(c)
