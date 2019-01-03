S=(raw_input())
c=0
a=[]
for i in range(0,len(S)):
    if(S[i].isspace()):
        c=c
        a.append(S[i])
    elif(c%2!=0):
        a.append(S[i])
        c=c+1
    else:
        a.append(S[i].upper())
        c=c+1
k="".join(map(str,a))
print(k)
