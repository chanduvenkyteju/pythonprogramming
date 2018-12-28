S=str(raw_input())
a=[]
for i in S:
    if(i not in a):
        a.append(i)
for i in a:
    if(S.count(i)==1):
        print(i,end=(""))
