n, m = map(int, input().split()) 

graph = [list(map(int, input().split())) for _ in range(n)]

def iterative_dfs(x, y):
    stack = [(x, y)]
    area = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while stack:
        x, y = stack.pop()
        
        if x < 0 or x >= n or y < 0 or y >= m:
            continue

        if graph[x][y] == 1:
            graph[x][y] = 0  
            area += 1  

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                stack.append((nx, ny))
    
    return area

count = 0
max_paint = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:  
            count += 1  
            max_paint = max(max_paint, iterative_dfs(i, j))  # 넓이 계산

print(count)
print(max_paint)