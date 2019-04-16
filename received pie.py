a = int(raw_input())
Np = [0] + [ int(x) for x in raw_input().split()]
Ns = [0 for i in range(0,a+4)]
np = 2
A = 0
B = 1
Nm = []
for i in range(0,a+1) :
    Nm.append([0,0])

for i in range(a,0,-1) :
    Ns[i] = Np[i] + Ns[i+1]
    if i == a :
        Nm[i][A] = Nm[i][B] = Np[i]
    else :
        Nm[i][A] = max(Nm[i + 1][A], Np[i] + Ns[i + 1] - Nm[i + 1][B])
        Nm[i][B] = max(Nm[i + 1][B], Np[i] + Ns[i + 1] - Nm[i + 1][B])
Amax = Ns[1] - Nm[1][B]
print(Amax, Nm[1][B])
