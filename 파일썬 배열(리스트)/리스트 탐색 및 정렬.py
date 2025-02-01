arr = [5, 3 ,8, 1, 2]

# 정렬 (오름차순)
arr.sort()
print(arr) # [1, 2, 3, 5, 8]

# 내림차순 정렬
arr.sort(reverse=True)
print(arr) # [8, 5, 3, 2, 1]

# 리스트 뒤집기
arr.reverse()
print(arr) # [1, 2, 3, 5, 8]

# 특정 값 개수 세기 (count)
print(arr.count(3)) # 1 (3이 한번 등장)

# 특정 값 찾기 (index)
print(arr.index(5)) # 3 (5의 위치)
