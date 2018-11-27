q=(raw_input())
p=0
for i in range(0,len(q)):
    if(q[i].isdigit() or q[i].isalpha() or q[i]==" "):
        p=p
    else:
        p=p+1
print(p)
