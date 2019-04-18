s=str(raw_input())
a=['a','e','i','o','u','A','E','I','O','U']
b=[]
c=[]
for i in range(0,len(s)):
    if(s[i] in a):
        b.append(s[i])
    else:
        c.append(s[i])
d=b+c
print("".join(d))
