from collections import deque

def solution(board):
    rows, cols = len(board), len(board[0])

    # 1) R(시작)와 G(목표)의 좌표를 먼저 찾는다
    start = None
    goal = None
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)

    if start is None or goal is None:
        return -1



    # 2) BFS용 방문 배열 (한 번 멈춘 지점을 기록)
    visited = [[False]*cols for _ in range(rows)]
    sx, sy = start
    visited[sx][sy] = True

    # 3) BFS 큐: (x, y, cnt) → cnt = 지금까지 슬라이딩한 횟수
    dq = deque()
    dq.append((sx, sy, 0))

    # 4) 상, 우, 하, 좌 순서(사방) 델타
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while dq:
        x, y, cnt = dq.popleft()
        # 만약 현재 (x, y)가 목표점이라면 그때까지의 cnt가 정답
        if (x, y) == goal:
            return cnt

        # 5) 네 방향으로 각각 한 번 “슬라이딩” 시도
        for dx, dy in directions:
            nx, ny = x, y
            # 벽이나 범위를 만날 때까지 곧장 이동
            while True:
                tx = nx + dx
                ty = ny + dy
                # 1) 보드를 벗어나거나, 2) 장애물 'D'를 만나면 멈추기 직전 위치가 (nx,ny)
                if tx < 0 or tx >= rows or ty < 0 or ty >= cols or board[tx][ty] == 'D':
                    break
                nx, ny = tx, ty

            # (nx, ny)가 “슬라이딩 이후 최종 멈춘 지점”이 된다
            # 만약 아직 방문하지 않았다면, cnt+1 이동으로 도달할 수 있다
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny, cnt + 1))

    # 빌 때까지 못 찾았다면 불가능
    return -1
