n=(raw_input()).split()
p=int(n[0])**2
q=int(n[1])**2
r=int(n[2])**2
if(p+q>=r):
    print("yes")
elif(q+r>=p):
    print("yes")
elif(p+r>=q):
    print("yes")
else:
    print("no")
