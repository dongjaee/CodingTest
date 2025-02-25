N,M=map(int,input().split())

time=list(map(int,input().split()))


start,end=max(time),sum(time)

while start<=end:
    mid=(start+end)//2

    total=0
    cnt=1
    for t in time:
        if total+t>mid:
            cnt+=1
            total=0
        total+=t

    if cnt<=M:
        ans=mid
        end=mid-1
    else:
        start=mid+1

print(ans)
    