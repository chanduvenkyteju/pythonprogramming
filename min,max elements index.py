N=int(raw_input())
a=(raw_input()).split()
b=[]
for i in a:
    b.append(int(i))
print(b.index(min(b))+1,b.index(max(b))+1)
