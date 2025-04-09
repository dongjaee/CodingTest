N=int(input())

record=[list(map(int,input().split())) for _ in range(N)]

result=[]
for x,y in record:
    cnt=0

    for i in range(N):
        if x<record[i][0] and y<record[i][1]:
            cnt+=1
    result.append(cnt+1)

print(" ".join(map(str,result)))