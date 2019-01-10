N=(raw_input())
M=(raw_input())
a=[]
if(M in N):
    a=N.replace(M,"")
for i in a:
    a=a.replace("  "," ")
print("".join(str(i) for i in a))  
