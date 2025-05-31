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
        min_value = min(min_value, matrix[x1][j])

    # (x1, y1) 위치에 저장해 두었던 원래 값을, 회전 후 빈 칸이 된 (x1, y1+1)에 넣어준다.
    matrix[x1][y1 + 1] = first

    return min_value
