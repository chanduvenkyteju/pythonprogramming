S=(raw_input()).split()
a=0
for i in S:
    if(a<len(S)):
        if(a%2==0):
            S[a]=i[::-1]
            a=a+1
        else:
            a=a+1
k=" ".join(map(str,S))
print(k)
