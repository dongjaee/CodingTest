N, M = map(int, input().split())
dot = list(map(int, input().split()))
dot.sort()  # 점들을 정렬하여 이진 탐색 가능하도록 함

# lower_bound: target 이상의 첫 위치 찾기
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# upper_bound: target 초과의 첫 위치 찾기
def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

for _ in range(M):
    start, end = map(int, input().split())

    # start 이상의 첫 번째 점 인덱스 찾기
    left_idx = lower_bound(dot, start)
    # end 초과의 첫 번째 점 인덱스 찾기
    right_idx = upper_bound(dot, end)

    print(right_idx - left_idx)