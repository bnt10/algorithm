def solution(grid):
    n, m = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    result = []

    # 방향: ↑→↓← (시계 방향)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 회전 결과 계산
    def turn(direction, cmd):
        if cmd == 'L':
            return (direction - 1) % 4
        elif cmd == 'R':
            return (direction + 1) % 4
        else:
            return direction

    for x in range(n):
        for y in range(m):
            for d in range(4):  # 모든 방향으로 출발
                if visited[x][y][d]:
                    continue

                cnt = 0
                cx, cy, cd = x, y, d

                while not visited[cx][cy][cd]:
                    visited[cx][cy][cd] = True
                    cnt += 1
                    cd = turn(cd, grid[cx][cy])
                    cx = (cx + dx[cd]) % n
                    cy = (cy + dy[cd]) % m

                result.append(cnt)

    return sorted(result)



def solution8(grid):

    n,m = len(grid) , len(grid[0])
    visited = [[[False]*4 for _ in range(m)  ]for _ in range(n) ]
    result = []
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    def turn(direction,cmd):
        if direction == 'L':
            return (direction - 1) % 4
        elif direction == 'R':
            return (direction + 1) % 4
        else:
            return direction

    for x in range(n):
        for y in range(m):
            for d in range(4):
                if visited[x][y][d]:
                    continue

                cnt = 0
                cx , cy ,cd = x, y ,d
                while not visited[cx][cy][cd]:
                    visited[cx][cy][cd] = True
                    cnt += 1

                    cd = turn(cd, grid[cx][cy])
                    cx = (cx + dx[cd]) % n
                    cy = (cy + dy[cd]) % m
                result.append(cnt)

    return sorted(result)