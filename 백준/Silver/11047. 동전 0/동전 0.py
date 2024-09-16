N,K = map(int,input().split())

money=[int(input()) for _ in range(N)]

cnt=0
for i in money[::-1]:
  if K//i>0:
    cnt+=K//i
    K=K%i
    
print(cnt)