X,Y=map(int,input().split())

left, right = 0, X 
Z = (Y * 100) // X
result = -1

while left <= right:
    mid = (left + right) // 2
    newZ = ((Y + mid) * 100) // (X + mid) 
    if newZ > Z:
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)