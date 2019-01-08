s=str(raw_input())
n='AaEeIiOoUu'
c=0
k=len(s)
for i in  range(0,k):
    if(s[i] in n):
        c=c+1   
    else:
        c=c
if(c>0):
    print("yes")
else:
    print("no")
