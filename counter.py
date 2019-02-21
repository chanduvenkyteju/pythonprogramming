n = int(raw_input())
p= 3
c = p
while(n>0):
    if(c == 0):
        p = 2*p
        c = p
    if(n==1):
        print(c)
        break
    n -= 1
    c -= 1
