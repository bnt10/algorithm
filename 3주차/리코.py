from collections import deque

def solution(maps):
    start_pos = end_pos = None
    rows, cols = len(maps), len(maps[0])

    for row in range(rows):
        for col in range(cols):
            if maps[row][col] == "R":
                start_pos = (row,col)
            if maps[row][col] == "G":
                end_pos = (row,col)

    if start_pos is None or end_pos is None :
        return -1

    start_x, start_y = start_pos
    dq = deque([(start_x,start_y,0)])
    visited = {start_pos}
    moves = [(-1,0),(0,1),(1,0),(0,-1)]
    while dq:
        x, y, depth = dq.popleft()
        if (x,y) == end_pos:
            return depth

        for dx,dy in moves:
            nx = x
            ny = y
            while True:
                tx = nx + dx
                ty = ny + dy
                if tx < 0 or tx >= rows or ty < 0 or ty >= cols or maps[tx][ty] == 'D':
                    break
                nx = tx
                ny = ty
            if (nx,ny) not in visited:
                visited.add((nx,ny))
                dq.append((nx,ny,depth + 1))
    return -1








print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))