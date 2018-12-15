N=int(raw_input())
a=(raw_input()).split()
for i in range(0,len(a)):
    x=a.count(a[i])
    if(x<2):
        print(a[i])
