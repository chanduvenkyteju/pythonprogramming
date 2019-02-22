n=int(raw_input())
k=(raw_input()).split()
s=[]
x,y=map(int,(raw_input()).split())
for i in k:
    s.append(int(i))
a=s.index(x)
b=s.index(y)
if(a>b):
    print(a-b)
else:
    print(b-a)
