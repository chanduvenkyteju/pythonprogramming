n=int(raw_input())
p=sorted(list(map(int,raw_input().split())))
q=[i for i in range (1,n+1)]
if(p==q):
    print("yes")
else:
    print("no")
