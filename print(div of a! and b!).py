a,b=map(int,(raw_input()).split())
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
p=fact(a)//fact(b)
print(p)
