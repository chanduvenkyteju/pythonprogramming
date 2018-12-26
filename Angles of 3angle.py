A=(raw_input()).split()
C=0
P=0
for i in A:
    if(int(i)==0):
        C=C+1
if((int(A[0])+int(A[1])+int(A[2]))==180):
    P=P+1
if(P==1 and C==0):
    print("yes")
else:
    print("no")
