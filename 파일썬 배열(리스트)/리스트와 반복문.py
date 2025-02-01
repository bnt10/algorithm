arr = [10, 20, 30, 40 ,50]

# 기본 for 문
for num in arr:
    print(num, end=" ") # 10, 20, 30, 40, 50

# 인덱스와 함께 순회 (enumerate)
for index, value in enumerate(arr):
    print(f"Index {index}: {value}")

# 리스트 컴프리핸션 (List Comprehension)
squared = [x**2 for x in arr]
print(squared) # [100, 400, 900, 1600, 2500]
