N=int(raw_input())
a=[]
for i in range(N,-1,-1):
    x=i+sum(list(map(int,str(i))))
    if (N==x):
        a.append(i)
    if (x<N-2):
        break
a.reverse()
print(len(a))
for i in a:
    print(i)
