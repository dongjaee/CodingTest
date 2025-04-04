import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

for x in range(19): 
    for y in range(19):  
        if board[x][y] != 0:
            color = board[x][y]
            for dx, dy in directions:
                cnt = 1
                nx = x + dx
                ny = y + dy

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
                    cnt += 1
                    if cnt > 5:
                        break
                    nx += dx
                    ny += dy

                if cnt == 5:
                    prev_x = x - dx
                    prev_y = y - dy
                    if 0 <= prev_x < 19 and 0 <= prev_y < 19 and board[prev_x][prev_y] == color:
                        continue

                    print(color)
                    print(x + 1, y + 1)
                    sys.exit(0)

print(0)