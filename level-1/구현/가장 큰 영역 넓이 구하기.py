N, M = 5, 5
board = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

move_map = [(-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)]
visited = [[False] * M for _ in range(N)]
maxSize = 0

def dfs(x, y):
    visited[x][y] = True

    for dx, dy in move_map:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and board[nx][ny] == 1:
                dfs(nx, ny)


island_count = 0
for x in range(N):
    for y in range(M):
        if board[x][y] == 1 and not visited[x][y]:
            dfs(x, y)
            island_count += 1
print(island_count)
