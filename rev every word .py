S=(raw_input()).split()
a=[]
for i in S:
    a.append(i[::-1])
K=" ".join(a)
print(K)
