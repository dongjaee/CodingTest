N=int(input())

liquid=list(map(int,input().split()))
liquid.sort()

left,right=0,N-1
closest_sum=float('inf')
answer=(0,0)


while left<right:
    mix=liquid[left]+liquid[right]

    if abs(mix)<abs(closest_sum):
        closest_sum=mix
        answer=(liquid[left],liquid[right])

    if mix>0:
        right-=1
    else:
        left+=1

print(answer[0],answer[1])