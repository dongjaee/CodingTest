N=int(input())
arr=list(map(int,input().split()))
M=int(input())

left, right = 0, max(arr)  
result = 0  

while left <= right:
    mid = (left + right) // 2 
    total = sum(min(mid, budget) for budget in arr) 

    if total <= M:  
        result = mid  
        left = mid + 1  
    else:  
        right = mid - 1  

print(result) 