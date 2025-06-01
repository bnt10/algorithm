# # 움직일 수 있는 건지 판단
# # bfs 구현
# # 움직이는 기능

from collections import deque

def solution(maps):
    dq = deque([(0,0,1)])
    visited = {(0,0)}
    width = len(maps) - 1
    height = len(maps[0]) - 1
    target = (width,height)
    move = [(-1,0),(0,1),(1,0),(0,-1)]


    def is_move(nx,ny):
        if 0 <= nx <= width and 0 <= ny <= height and maps[nx][ny] == 1:
            return True
        return False

    while dq:
        x,y,depth = dq.popleft()
        if (x,y) == target:
            return depth
        for dx,dy in move:
            nx = x + dx
            ny = y + dy
            if is_move(nx,ny) and (nx,ny) not in visited:
                visited.add((nx,ny))
                dq.append((nx,ny,(depth + 1 )))
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

#dist 별도 배열 활용
from collections import deque

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    rows, cols = len(maps), len(maps[0])
    if maps[0][0] == 0 or maps[rows-1][cols-1] == 0:
        return False

    # 상하좌우 델타
    moves = [(-1,0), (0,1), (1,0), (0,-1)]

    # dist 배열: 0=미방문, 양수=시작점으로부터 거리
    dist = [[0] * cols for _ in range(rows) ]
    dist[0][0] = 1

    dq = deque([(0, 0)])


    while dq:
        x, y = dq.popleft()
        # 목표에 도달했으면 dist[x][y] 반환
        if (x, y) == (rows-1, cols-1):
            return dist[x][y]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            # 경계 + 이동 가능 + 아직 방문하지 않은 칸(dist==0)인지 확인
            if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] == 1 and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                dq.append((nx, ny))

    return -1
