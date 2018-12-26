def rot(S,K):
    print(S[K:]+S[:K])
S,K=map(str,(raw_input()).split())
K=int(K)
m=len(S)-K
rot(S,m)
