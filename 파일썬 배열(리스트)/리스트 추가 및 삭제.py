arr = [1, 2, 3]

# 요소 추가(append: 리스트 끝에 추가)
arr.append(4)
print(arr) # [1, 2, 3, 4]

# 특정 위치에 요소 삽입 (insert (index 값)
arr.insert(1,99)
print(arr) # [1, 99, 2, 3, 4]

# 요소 삭제 (remove: 특정 값 삭제)
arr.remove(99)
print(arr) # [1, 2, 3, 4]

# 요소 삭제 (pop: 마지막 요소 제거 및 반환)
last_element = arr.pop()
print(arr) # [1, 2, 3]
print(last_element) # 4

# 특정 위치 요소 삭제 (del)
del arr[1]
print(arr) # [1, 3]
