S=str(raw_input())
a=[]
for i in S:
    if(i not in a):
        a.append(i)
print("".join(a)) 
