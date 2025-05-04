"""
2차원 맵에서 상하좌우로 이동하면서 조건을 만족하는 경로를 탐색하는 것

방향백터를 정해두고
현재 위치 (x, y) 에서 이동할 수 있는 곳으로 재귀적으로 읻동
이미 방문한 곳은 다시 가지 않도록 visited 체크


"""
# 기본 뼈대 코드

N,M = 5,5
board = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1]
]

visited = [[False] for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    visited[x][y] = True

    for i in  range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny <= M:
            if not visited[nx][ny] and board[nx][ny] == 0:
                dfs(nx,ny)

dfs(0,0)