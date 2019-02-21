n=int(raw_input())
a=[]
c=0
p=['a','e','i','o','u','A','E','I','O','U']
for i in range(0,n):
    a.append(str(input()))
    for j in a[i]:
        if(j in p):
            c=c+1
if(c>0):
    print("yes")
else:
    print("no")
