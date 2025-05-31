"""
행렬을 1씩 증가하는 행렬

"""

rows = 5
columns  = 5

matrix = [[i * columns + (j + 1) for j in range(columns)]  for i in range(rows)]

#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
print(matrix)
