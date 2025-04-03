from itertools import permutations

k=int(input())
arr=input().split()

nums=[i for i in range(10)]
ans=[]

for perm in permutations(nums,k+1):
    for i in range(k):
        if arr[i]=='<':
            if perm[i]>=perm[i+1]:
                break
        elif arr[i]=='>':
            if perm[i]<=perm[i+1]:
                break

    else:
        ans.append(''.join(map(str,perm)))

print(max(ans))
print(min(ans))