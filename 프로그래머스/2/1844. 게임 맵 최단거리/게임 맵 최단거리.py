from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    q=deque([(0,0)])
    
    # 상, 하, 좌, 우 방향 정의
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        x,y=q.popleft()
        
        
        for dx,dy in directions:
            nx,ny=x+dx, y+dy
            
            #경로 밖에 나감 or 벽이면 짤
            if nx<0 or nx>=n or ny<0 or ny>=m or maps[nx][ny]==0:
                continue
                
            if maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                q.append((nx,ny))
                
    return maps[n-1][m-1] if maps[n-1][m-1]>1 else -1
    
    