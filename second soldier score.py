def fact(n) :
    L = []
    i = 2
    c = 0
    while n >1 :
        while n%i == 0 :
            c += 1
            n //= i
        i += 1
    return c
n = int(raw_input())
L = [(raw_input()).split() for i in range(0,n)]
for i in range(0,n) :
    p = 1
    n, k = L[i]
    n, k = int(n), int(k)
    for i in range(k+1,n+1) :
        p = p*i
    a = fact(p)
    print(a)
