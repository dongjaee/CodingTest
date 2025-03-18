import sys
sys.setrecursionlimit(1000)


def dfs(x,y):
    dir=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

    field[x][y]=0
    for dx,dy in dir:
        nx=x+dx
        ny=y+dy
        if 0<=nx<h and 0<=ny<w and field[nx][ny]==1:
            dfs(nx,ny)
        
while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    field=[]
    cnt=0

    for _ in range(h):
        field.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if field[i][j]==1:
                dfs(i,j)
                cnt+=1

    print(cnt)