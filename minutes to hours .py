t=int(input())
if t > 0:
    t = "%d:%d"%(t // 60, t % 60)
print(t)
