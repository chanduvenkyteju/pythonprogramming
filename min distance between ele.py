n= int(raw_input())
a = list(map(int,(raw_input()).split()))
u,v = map(int,(raw_input()).split())
x =[index for index, value in enumerate(a) if value == u]
y = [index for index, value in enumerate(a) if value == v]
k = n
for i in range(len(x)):
    for j in range(len(y)):
        if(x[i]>y[j]):
            d = x[i]-y[j]
        else:
            d = y[j]-x[i]
        if(d<k):
            k = d
print(k)
