N,M=map(int,input().split())
board=[list(input()) for _ in range(N)]

result=0

for i in range(N):      #세로 탐색 i=세로
    for j in range(M):  #가로 탐색 j=가로

        if N>M:
            for a in range(2,M+1):
                if i+a<=N and j+a<=M:
                    if len({board[i][j], board[i+a-1][j], board[i][j+a-1], board[i+a-1][j+a-1]})==1:
                        result=max(result,a**2)
                    
        else:
            for a in range(2,N+1):
                if i+a<=N and j+a<=M:
                    if len({board[i][j], board[i+a-1][j], board[i][j+a-1], board[i+a-1][j+a-1]})==1:
                        result=max(result,a**2)


if result==0:
    print(1)
else:
    print(result)