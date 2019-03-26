n=int(raw_input())
a=(raw_input().split())
a.sort()
l=[]
s=[]
for i in a:
    l.append(len(i))
l.sort()
for x in l:
    for y in a:
        if(len(y)==x):
            if y not in s:
                s.append(y)
print(" ".join(s))
