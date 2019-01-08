N=str(raw_input())
a=[]
for i in range(0,len(N)):
    if(N[i].isnumeric()):
        a.append(N[i])
print("".join(str(i) for i in a))  
