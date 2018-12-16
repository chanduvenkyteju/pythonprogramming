S=(raw_input()).split()
c=[]
for i in S:
    c.append(i[::-1])
s=" ".join(c)
print(s)
