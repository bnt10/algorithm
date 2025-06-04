from collections import deque

def solution(maps):
    rows,cols = len(maps), len(maps[0])

    moves = [(-1,0),(0,1),(1,0),(0,-1)]
    visited = {(0,0)}
    dq = deque([(0,0,0)])
    is_open = False
    is_start = False
    while dq:
        x,y,depth = dq.popleft()
        if is_open == False and maps[x][y] == "S":
            is_open  = False
            is_start = True
            visited.clear()
            visited.add((x,y))
            dq.append((x,y,0))

        if is_start and maps[x][y] == "L":
            is_open = True
            visited.clear()

        if is_start and is_open and maps[x][y] == "E":
            return depth

        for dx,dy in moves:
            nx, ny = x + dx , y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] != "X"  and (nx,ny) not in visited:
                visited.add((nx,ny))
                dq.append((nx,ny,(depth + 1)))
    return -1

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print("S -> O - > E - > O -> L -> O -> E : 6")