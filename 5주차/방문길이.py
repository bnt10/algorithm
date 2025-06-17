# 방문 좌표가 아니 방문 path를 기록하는 방법
# path의 경우 시작 점, 끝점이 서로 바뀌게 들어 올 수 있기 때문에 이를 하나의 좌표로 표현하는 방법을 알아야 합니다.
# path = ((sx,sy), (nx,ny)) if (sx,sy) < (nx,ny) else ( (nx, ny) , (sx,sy) )
def solution(dirs):
    answer = 0
    sx, sy = 0,0
    visited = set()

    move = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }

    for d in dirs:
        dx,dy = move[d]
        nx , ny = sx + dx , sy + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:

            path = ((sx,sy),(nx,ny)) if (sx ,sy) < (nx, ny) else ((nx,ny),(sx,sy))
            if path not in visited:
                visited.add(path)
                answer += 1
            sx = nx
            sy = ny


    return answer

print(solution("UUD"))