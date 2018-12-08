N=int(raw_input())
s=input().split()
c=1
for i in range(1,len(s)-1):
    if(s[i]<=s[i+1]):
        c=c+1
if(c==len(s)):
    print("yes")
else:
    print("no")
