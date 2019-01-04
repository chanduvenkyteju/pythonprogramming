S=str(raw_input())
a=[]
for i in S:
    if(i not in a):
        a.append(i)
a=a[::-1]
S1="".join(map(str,a))
print(S1)
