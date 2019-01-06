N=str(raw_input())
a=list(N)
s=''
a.sort()
s=s+a.pop()
n=len(a)
for i in range(0,n):
    s=s+a[i]
if(int(N)<int(s)):
    print(s)
else:
    print("impossible")
