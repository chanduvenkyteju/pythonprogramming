s=str(raw_input())
a=[]
for i in range (0,len(s)):
    a.append(s.count(s[i]))
k=a.index(max(a))
print(s[k])
