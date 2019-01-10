N=(raw_input())
M=(raw_input())
a=[]
l=int(len(a))
if(M in N):
    a=N.replace(M,"")
if(a[0]==" "):
    a=a.replace(" ","")    
for i in a:   
    a=a.replace("  "," ")        
print("".join(str(i) for i in a))
