# 📝 itertools 모듈 요약 노트 (순열과 조합)

---

## 🔑 **기초 개념**

* **모듈 이름**: `itertools`
* **용도**: 반복 가능한(iterable) 객체를 처리하는 효율적인 도구 제공

| 개념               | 정의 및 특징                  | 예시                |
| ---------------- | ------------------------ | ----------------- |
| 순열(permutations) | 원소를 나열하는 모든 경우의 수 (순서 O) | `(A,B)` ≠ `(B,A)` |
| 조합(combinations) | 원소를 선택하는 모든 경우의 수 (순서 X) | `(A,B)` = `(B,A)` |

---

## 🔢 **주요 함수 정리**

### ① permutations (순열)

* 형식:

```python
itertools.permutations(iterable, r=None)
```

* 설명: 길이 `r`인 모든 가능한 순서의 조합(순열)을 생성
* 반환형: **튜플** 형태의 iterator
* 특징:

    * 순서 고려 (다른 순서 = 다른 원소 취급)
    * 원소 개수보다 큰 순열 생성 불가능

**예제 코드**

```python
from itertools import permutations

items = ['X', 'Y', 'Z']
result = list(permutations(items, 2))

print(result)
# [('X', 'Y'), ('X', 'Z'), ('Y', 'X'), ('Y', 'Z'), ('Z', 'X'), ('Z', 'Y')]
```

---

### ② combinations (조합)

* 형식:

```python
itertools.combinations(iterable, r)
```

* 설명: 길이 `r`인 모든 가능한 조합을 생성 (순서 무관)
* 반환형: **튜플** 형태의 iterator
* 특징:

    * 순서 무시 (같은 원소끼리 중복 없음)
    * 원소 개수보다 큰 조합 생성 불가능

**예제 코드**

```python
from itertools import combinations

items = ['X', 'Y', 'Z']
result = list(combinations(items, 2))

print(result)
# [('X', 'Y'), ('X', 'Z'), ('Y', 'Z')]
```

---

## ⚠️ **주의할 점**

* iterable 내 **중복된 원소**는 각각 개별적인 원소로 취급함.

**중복 원소 예시 코드**

```python
from itertools import permutations, combinations

items = [1, 2, 2]

print(list(permutations(items, 2)))
# [(1, 2), (1, 2), (2, 1), (2, 2), (2, 1), (2, 2)]

print(list(combinations(items, 2)))
# [(1, 2), (1, 2), (2, 2)]
```

---

## 📌 **활용 사례**

프로그래머스 Lv.1 **두 개 뽑아서 더하기** 문제를 itertools 활용하여 해결한 예제:

```python
from itertools import combinations

def solution(numbers):
    # 가능한 두 수의 모든 조합의 합 계산 후 중복 제거 및 정렬
    return sorted(set(a + b for a, b in combinations(numbers, 2)))

# 테스트 예시
print(solution([2, 1, 3, 4, 1]))  # [2, 3, 4, 5, 6, 7]
```

---

## 🚩 **요약 정리 표**

| 함수           | 사용 예시                    | 예시 결과                                                                      |
| ------------ | ------------------------ | -------------------------------------------------------------------------- |
| permutations | `permutations("ABC", 2)` | `[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]` |
| combinations | `combinations("ABC", 2)` | `[('A', 'B'), ('A', 'C'), ('B', 'C')]`                                     |

* **순서 중요 → permutations**
* **순서 무시 → combinations**

---

## 🎯 **최종 복습 미션 (반드시 수행)**

* [ ] permutations와 combinations의 차이점 직접 메모
* [ ] 리스트 `[3,4,5,6]`을 활용하여 길이 2의 순열과 조합 **각 3가지** 예시 작성
* [ ] 중복 원소 포함 `[1, 2, 2]`을 활용하여 permutations와 combinations 테스트 후 결과 기록
* [ ] [공식문서 itertools](https://docs.python.org/3/library/itertools.html)에서 **`product`** 함수의 예제 1개를 추가 학습하여 노트에 기록

---

