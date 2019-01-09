N,M=map(int,input().split())
P,Q=map(int,input().split())
N=N*60+M
P=P*60+Q
K=abs(N-P)
print(K//60,K%60)
