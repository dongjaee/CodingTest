import sys
sys.setrecursionlimit(10000)

M,N,K=map(int,input().split())

result=[]
def dfs(x,y):
    directions=[(1,0),(-1,0),(0,1),(0,-1)]

    field[x][y]=1
    area=1
    for dx,dy in directions:
        nx=x+dx
        ny=y+dy
        if 0<=nx<M and 0<=ny<N and field[nx][ny]==0:
            area+=dfs(nx,ny)

    return area

field=[[0]*N for _ in range(M)]

for _ in range(K):
    arr=list(map(int,input().split()))
    for i in range(arr[1],arr[3]):
        for j in range(arr[0],arr[2]):
            if field[i][j]==0:
                field[i][j]=1

cnt=0
result=[]
for i in range(M):
    for j in range(N):
        if field[i][j]==0:
            result.append(dfs(i,j))
            cnt+=1

result.sort()
print(cnt)
print(" ".join(map(str,result)))