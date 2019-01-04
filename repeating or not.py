N=(raw_input())
a=[]
for i in N:
    if(i not in a):
        a.append(i)
a="".join(a)
if(N==a):        
    print("no")
else:
    print("yes")
