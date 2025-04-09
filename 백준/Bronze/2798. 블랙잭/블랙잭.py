from itertools import combinations

N,M=map(int,input().split())
nums=map(int,input().split())

result=0 

for i in combinations(nums,3):
    if sum(i)==M:
        print(M)
        break
    if sum(i)<M:
        result=max(result,sum(i))
else:
    print(result)
