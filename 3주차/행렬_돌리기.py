def rotate(x1, x2, y1, y2, matrix):
    # (x1, y1) 위치의 원소를 미리 저장해 둔다.
    first = matrix[x1][y1]
    min_value = first  # 테두리 이동 중 최소값을 추적하기 위해 사용

    # 1) 왼쪽(Left) → 아래(Down) 구간으로 한 칸씩 위→아래로 이동
    for i in range(x1, x2):
        matrix[i][y1] = matrix[i + 1][y1]
        min_value = min(min_value, matrix[i][y1])

    # 2) 아래(Bottom) → 오른쪽(Right) 구간으로 한 칸씩 왼→오 방향으로 이동
    for j in range(y1, y2):
        matrix[x2][j] = matrix[x2][j + 1]
        min_value = min(min_value, matrix[x2][j])

    # 3) 오른쪽(Right) → 위(Up) 구간으로 한 칸씩 아래→위 방향으로 이동
    for i in range(x2, x1, -1):
        matrix[i][y2] = matrix[i - 1][y2]
        min_value = min(min_value, matrix[i][y2])

    # 4) 위(Top) → 왼쪽(Left) 구간으로 한 칸씩 오→왼 방향으로 이동
    for j in range(y2, y1, -1):
        matrix[x1][j] = matrix[x1][j - 1]
        min_value = min(min_value, matrix[x1][j-1])

    # (x1, y1) 위치에 저장해 두었던 원래 값을, 회전 후 빈 칸이 된 (x1, y1+1)에 넣어준다.
    matrix[x1][y1 + 1] = first

    return min_value


def rotate(x1,y1,x2,y2,metrix):
    first = metrix[x1][y1]
    min_value = first

    #아래
    for i in range(x1,x2):
        metrix[i][y1] = metrix[i+1][y1]
        min_value = min(min_value,metrix[i+1][y1])

    #왼쪽
    for i in range(y1,y2):
        metrix[x2][i] = metrix[x2][i+1]
        min_value = min(min_value,metrix[x2][i+1])

    #위
    for i in range(x2,x1,-1):
        metrix[i][y2] = metrix[i-1][y2]
        min_value = min(min_value,metrix[i-1][y2])
    #오른쪽
    for i in range(y2,y1+1,-1):
        metrix[x1][i] = metrix[x1][i-1]
        min_value = min((min_value,metrix[x1][i-1]))

    metrix[x1][y1+1] = first
    return min_value


#version2
def solution(rows, columns, queries):
    answer = []
    board = [[ columns * j+ (i + 1) for j in range(columns) ] for i in range(rows)]
    for query in queries:
        a,b,c,d = query[0] -1 , query[1] - 1, query[2] -1 , query[3] -1
        row1, row2 = board[a][b:d] , board[c][b+1:d+1]
        _min = min(row1 + row2)

        for i in range(c, a , -1):
            board[i][d] =board[i-1][d]
            if board[i][d] < _min : _min = board[i][d]
        for i in range(a,c):
            board[i][b] = board[i + 1][b]
            if board[i][b] < _min : _min = board[i][b]

        board[a][b + 1 : d + 1] , board[c][b:d] = row1, row2

        answer.append(_min)
    return answer



def rotate2(x1,x2,y1,y2,matrix):
    # 인플레이스 방식으로 으로 하면 추가 메모리를 최소화 할 수 있다 그냥 버퍼를 활용하는 방식은
    # 돌려야 하는 테투리를 버퍼에 담아놓고 읻동 후 삽입해주는 과정이 필요하게 된다
    first = matrix[x1][y1]
    min_value = first

    for k in range(x1,x2):
        matrix[k][y1] = matrix[k+1][y1]
        min_value = min(min_value, matrix[k+1][y1])

    for k in range(y1,y2):
        matrix[x2][k] = matrix[x2][k+1]
        min_value = min(min_value, matrix[x2][k+1])

    for k in range(x2,x1,-1):
        matrix[k][y2] = matrix[k-1][y2]
        min_value = min(min_value,matrix[k-1][y2])

    for k in range(y2,y1+1,-1):
        matrix[y1][k] = matrix[y1][k-1]
        min_value = min(min_value,matrix[y1][k-1])

    matrix[x1][y1+1] = first
    return  min_value

