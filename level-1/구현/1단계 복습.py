from math import floor

N = 4
T = 2
temp_map = [
    [10,5,20,10],
    [15,30,10,25],
    [20,15,5,30],
    [10,5,20,15]
]

move_map = [(-1,0),(1,0),(0,-1),(0,1)]

def is_move(x,y):
    return 0 <= x <= N and 0 <= y < N


for _ in range(T):
    pre_board = [row[:] for row in temp_map]
    changes = []
    for x in range(N):
        for y in range(N):
            for dx,dy in move_map:
                nx, ny = x + dx , y + dy

                if is_move(nx,ny):
                   current_value = pre_board[x][y]
                   compare_value = pre_board[dx][dy]
                   if abs(current_value -compare_value) > 3:
                        mean = floor((current_value + compare_value) / 2 )
                        changes.append(((x,y),mean))
                        changes.append(((dx,dy),mean))
    for (x,y), val in changes:
        temp_map[x][y] = val

total_temp = sum(map(sum,temp_map))