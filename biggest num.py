N=int(raw_input())
p=(raw_input()).split()
p.sort()
S=0
s=len(p)
while(s>0):
    b=int(p[s-1])
    S=S*10+b
    s=s-1
print(S)
