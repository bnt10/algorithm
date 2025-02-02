"""
itertools에 모듈에 포함된 조합(Combinations)을 생성하는 함수입니다.

사용법:
 combinations(iterable, r) 형태로 사용하며, iterable에서 중복 없이 r개
 를 선택하는 모든 조합을 반환합니다.
특징:
 순서를 고려하지 않고(즉, 순열이 아닌 조합), 결과는 정렬된 순서의 튜퓨형태로 제공됩니다.
"""

from itertools import combinations

data = [1, 2, 3 ,4]
r = 2

# data에서 2개를 뽑는 모든 조합 구하기
for comb in combinations(data, 2):
    print(comb)
"""
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
"""