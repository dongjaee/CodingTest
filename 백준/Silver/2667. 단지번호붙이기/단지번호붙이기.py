N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

cnt = 0  
result = []  

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:  
            cnt += 1 
            house = 0  
            stack = [(i, j)]
            visited[i][j] = True

            while stack:
                x, y = stack.pop()
                house += 1  

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy  
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == 1:
                        visited[nx][ny] = True
                        stack.append((nx, ny))

            result.append(house)  


result.sort()
print(cnt)
for r in result:
    print(r)