def fact(N) :
    p = 1
    for i in range(1,N+1) :
        p = p * i
    return p
N,K = (raw_input()).split()
N,K = int(N),int(K)
ans = fact(N) // (fact(K) * fact(N-K))
print(ans)
