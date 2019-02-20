n=(raw_input())
s=0
a=2
if(len(n)>1):
    for i in range(0,len(n)):
        if(a<=len(n)):
            s=s+int(n[i])**a
            a=a+1
        else:
            s=s+int(n[i])**1
else:
    s=int(n[0])**2
print(s)
    
