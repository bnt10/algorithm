arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# [표현식 for 변수 in 반복 가능한 객체 if 조건]
# if 조건을 통과하는 경우에만 표현식이 적용
even_numbers = [x for x in arr if x % 2 == 0]
print(even_numbers) # [2, 4, 6, 8, 10]

even_numbers_2 = [x % 2 == 0   for x in arr]
print(even_numbers_2) # [False, True, False, True, False, True, False, True, False, True]