a,b=map(int,(raw_input()).split())
c=0
for i in range(a,b):
    if(int(i**0.5)==i**0.5):
        c=c+1
    else:
        c=c
print(c)
