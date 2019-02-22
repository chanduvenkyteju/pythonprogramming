p=(raw_input())
q=(raw_input())
a=[]
for i in p:
    if(i in q and i not in a):
        a.append(i)
k="".join(map(str,a))
print(k)
