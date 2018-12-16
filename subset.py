N,M=map(int,(raw_input()).split())
A=(raw_input()).split()
B=(raw_input()).split()
A.sort()
B.sort()
s1=''.join(A)
s2=''.join(B)
if(s2 in s1):
    print("YES")
else:
    print("NO")
