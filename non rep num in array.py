N=int(raw_input())
a=list(map(int,(raw_input()).split()))
for i in a:
    if(a.count(i)==1):
        print(i)
