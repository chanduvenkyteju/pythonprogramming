N=(raw_input())
L=len(N)
s=list(N)
if(L%2==0):
    a=L/2 - 1
    k=int(a)
    s[k]='*'
    s[k+1]='*'
else:
    a=L/2 - 1
    k=int(a)
    s[k+1]='*'
print("".join(s))
