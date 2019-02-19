def rem(a):
    res =[]
    for i in range(len(a)):
        if(i%2 != 0):
            res.append(a[i])
    return res
n = int(input())
a = list(map(int,input().split()))
k= a
while(len(a)>1):
    a = rem(a)
print(k.index(a[0]))
