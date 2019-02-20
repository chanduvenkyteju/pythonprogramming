n=int(raw_input())
a=list(map(str,(raw_input()).split()))
a.sort()
for i in range(0,n):
    a[i]=a[i].lower()   
for i in a:
    print(i)
