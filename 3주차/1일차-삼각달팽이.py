def solution(n):
    # 1) 삼각형 모양의 2차원 배열 생성 (길이가 1, 2, ..., n인 행을 가진 이중리스트)
    triangle = [ [0] * (i + 1) for i in range(n) ]

    # 2) 초기 변수 선언
    #    - 총 채워야 할 숫자 개수(사용은 별도 불필요, 주로 디버깅용)
    total = n * (n + 1) // 2

    #    - 시작 좌표: (-1, 0)으로 두면 첫 루프에서 아래로 한 칸 이동 시 (0,0)이 된다.
    x, y = -1, 0

    #    - 채울 숫자: 1부터 시작해서 total까지 증가
    num = 1

    #    - 방향 인덱스: 0 → 아래, 1 → 오른쪽, 2 → ↖(위-왼쪽)
    dir_idx = 0

    #    - 방향별 이동 변화량 정의
    dx = [1, 0, -1]   # 아래 → (x+1, y),   오른쪽 → (x+0, y+1),   ↖ → (x-1, y-1)
    dy = [0, 1, -1]

    #    - "한 번에 몇 칸을 이동해서 채울 것인지" (처음에는 n칸, 그다음엔 n-1칸, ...)
    length = n

    # 3) 달팽이 모양으로 수 채우기
    while length > 0:
        # 3-1) 현재 방향(dir_idx)으로 length번만큼 한 칸씩 이동하며 숫자를 채운다.
        for _ in range(length):
            x += dx[dir_idx]
            y += dy[dir_idx]
            triangle[x][y] = num
            num += 1

        # 3-2) 현재 방향이 끝났으므로 남은 횟수 한 칸 줄이고, 방향을 다음으로 전환
        length -= 1
        dir_idx = (dir_idx + 1) % 3

    # 4) 2차원 배열을 1차원 배열로 변환
    #    sum(triangle, [])를 사용하면 [[1],[2,9],[3,10,8],...]를 [1,2,9,3,10,8,...]로 펼쳐준다.
    return sum(triangle, [])


# 삼각형 배열을 만드는 방법
"""
[0]
[0][0]
[0][0][0]
"""
n =3
triangle = [ [0] * i for i in range(1,n+1)]
print(triangle)


def solution(n):
    dy = [0,1,-1]
    dx = [1,0,-1]
    snail = [[0] * i for i in range(1, n + 1)]
    x = y = angle = 0
    cnt = 1
    size = ( n + 1) * n // 2

    while cnt <= size:
        snail[y][x] = cnt
        ny = y + dy[angle]
        nx = x + dx[angle]
        cnt += 1

        if 0 <= ny < n and 0 <= nx < ny and snail[ny][nx] == 0:
            y,x = ny, nx
        else:
            angle = (angle + 1) % 3
            y += dy[angle]
            x += dx[angle]

    return [i for j in snail for i in j]