N= int(raw_input())
s = 0
for j in range(0,N):
    k = list(map(int,(raw_input()).split()))
    s = s+ sum(k)
count = N*N
a = s/count
print("{0:.6f}".format(round(a,6)))
