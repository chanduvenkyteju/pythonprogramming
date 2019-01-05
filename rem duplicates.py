N=int(raw_input())
a=(raw_input()).split()
b=[]
for i in a:
    if(i not in b):
        b.append(i)
print(" ".join(b)) 
