from collections import deque

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    result = []
    visited = set()
    def bfs_count(start_x,start_y,curr):
        dq = deque([(start_x,start_y)])
        count = int(curr)
        visited.add((start_x,start_y))
        moves = [(-1,0),(0,1),(1,0),(0,-1)]
        while dq:
            x, y = dq.popleft()

            for dx,dy in moves:
                nx,ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] != 'X' and not (nx,ny) in visited :
                        visited.add((nx,ny))
                        dq.append((nx,ny))
                        count += int(maps[nx][ny])
        return  int(count)


    for row in range(rows):
        for col in range(cols):
            if (row,col) in visited or maps[row][col] == 'X':
                continue

            sum_count = bfs_count(row,col, int(maps[row][col]))
            if sum_count > 0:
                result.append(sum_count)

    return  [-1] if len(result) == 0 else sorted(result)
print(solution(["X591X","X1X5X","X231X", "1XXX1"]	))