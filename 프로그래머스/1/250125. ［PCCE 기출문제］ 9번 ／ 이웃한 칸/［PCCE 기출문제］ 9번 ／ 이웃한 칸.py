def solution(board, h, w):
    start = board[h][w]
    cnt = 0  # 인접한 같은 색깔 칸의 개수를 저장

    # 상하좌우 방향 설정
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 각 방향을 탐색
    for dh, dw in directions:
        nh, nw = h + dh, w + dw

        # 인접 칸이 보드의 범위를 벗어나지 않는지 확인
        if 0 <= nh < len(board) and 0 <= nw < len(board[0]):
            # 인접 칸의 색상이 시작 칸과 같으면 카운트 증가
            if board[nh][nw] == start:
                cnt += 1

    return cnt