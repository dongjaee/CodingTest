import sys

N=int(sys.stdin.readline())
P=list(map(int,sys.stdin.readline().split()))
P.sort()
result=0
P_i=0
for i in P:
  P_i+=i
  result+=P_i
  

print(result)