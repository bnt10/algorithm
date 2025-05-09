**배열과 dict 개념 정리**

배열과 dict는 자료구조에서 매우 중요한 역할을 합니다. 배열은 순차적으로 데이터를 저장하고, index를 통해 접근할 수 있습니다. dict는 키-값 쌍으로 데이터를 저장하며, 키를 사용해 값을 빠르게 조회할 수 있습니다.

* **자주 쓰는 배열 메서드**

    * `append(x)`: 요소를 추가
    * `extend(iterable)`: Iterable을 추가
    * `pop(index)`: 인덱스로 요소 제거
* **자주 쓰는 dict 메서드**

    * `get(key)`: 키 값 조회
    * `keys()`: 모든 키 반환
    * `values()`: 모든 값 반환

---

## 📚 배열(List) 요약

### 1. 기본 연산

* **인덱싱 / 슬라이싱**

  ```python
  a = [1,2,3,4,5]
  a[0], a[-1]          # 1, 5
  a[1:4], a[:3], a[::2]  # [2,3,4], [1,2,3], [1,3,5]
  ```
* **길이 / 포함 여부**

  ```python
  len(a)               # 5
  3 in a              # True
  ```

### 2. 자주 쓰는 메서드

| 메서드                   | 용도                        | 시간 복잡도     | 예시                      |
| --------------------- | ------------------------- | ---------- | ----------------------- |
| `append(x)`           | 맨 뒤에 원소 추가                | O(1)       | `a.append(6)`           |
| `extend(iter)`        | 다른 iterable의 모든 원소를 뒤에 추가 | O(k)       | `a.extend([7,8])`       |
| `insert(i, x)`        | 인덱스 i 위치에 원소 삽입           | O(n)       | `a.insert(2,99)`        |
| `pop()` / `pop(i)`    | 맨 뒤(or i 위치) 원소 제거 & 반환   | O(1)/O(n)  | `a.pop()`, `a.pop(1)`   |
| `remove(x)`           | 첫 번째로 나오는 x 제거            | O(n)       | `a.remove(3)`           |
| `index(x)`            | 첫 번째 x 위치 반환              | O(n)       | `a.index(4)`            |
| `count(x)`            | x의 등장 횟수                  | O(n)       | `a.count(2)`            |
| `sort()` / `sorted()` | 제자리 정렬 / 새로운 정렬 리스트 반환    | O(n log n) | `a.sort()`, `sorted(a)` |
| `reverse()`           | 제자리 뒤집기                   | O(n)       | `a.reverse()`           |
| `copy()`              | 얕은 복사                     | O(n)       | `b = a.copy()`          |
| `clear()`             | 모든 원소 제거                  | O(n)       | `a.clear()`             |

### 3. 유용한 팁

* **리스트 컴프리헨션**

  ```python
  # 간결하고 빠른 생성
  squares = [x*x for x in range(10) if x%2==0]
  ```
* **`enumerate()`** 로 인덱스와 값 동시 반복

  ```python
  for i, v in enumerate(a):
      print(i, v)
  ```
* **`zip()`** 으로 여러 리스트 병렬 처리

  ```python
  for x, y in zip(list1, list2):
      ...
  ```
* **슬라이싱 복사**

  ```python
  b = a[:]   # 얕은 복사
  ```
* **빈번한 값 계산** 은 `collections.Counter` 사용

  ```python
  from collections import Counter
  cnt = Counter(a)    # 값별 등장 횟수 딕셔너리
  ```

---

## 🔑 사전(Dict) 요약

### 1. 기본 연산

* **키 조회 / 값 불러오기**

  ```python
  d = {'a':1, 'b':2}
  d['a'], d.get('c', 0)   # 1, 0 (`get`은 기본값 지정 가능)
  ```
* **길이 / 포함 여부**

  ```python
  len(d)               # 2
  'b' in d            # True
  ```

### 2. 자주 쓰는 메서드

| 메서드                                    | 용도                        | 시간 복잡도        | 예시                                    |
| -------------------------------------- | ------------------------- | ------------- | ------------------------------------- |
| `dict.keys()`, `.values()`, `.items()` | 키 / 값 / (키,값) 튜플 반복       | O(n)          | `for k,v in d.items(): ...`           |
| `get(k, default)`                      | 키가 없을 때 기본값 반환            | O(1)          | `d.get('x',0)`                        |
| `setdefault(k, v)`                     | 키가 없으면 v로 추가, 있으면 기존 값 반환 | O(1)          | `d.setdefault('a',10)`                |
| `pop(k)`                               | 키 k 제거 후 값 반환             | O(1)          | `d.pop('b')`                          |
| `popitem()`                            | 임의의 (키,값) 제거 후 반환         | O(1)          | `d.popitem()`                         |
| `update(other_dict)`                   | 다른 dict 병합 (기존 키 덮어쓰기)    | O(len(other)) | `d.update({'c':3})`                   |
| `clear()`                              | 모든 키-값 제거                 | O(n)          | `d.clear()`                           |
| **dict comprehension**                 | 조건·변환을 적용한 새 dict 생성      | O(n)          | `{k:v*2 for k,v in d.items() if v>1}` |

### 3. 유용한 팁

* **키 순회가 필요 없으면** `.values()` 만 사용해 불필요한 튜플 해제 방지
* **`defaultdict`** 로 키 존재 여부 검사 생략

  ```python
  from collections import defaultdict
  dd = defaultdict(int)   # 기본값 0
  dd['x'] += 1
  ```
* **`Counter`** 는 사실상 `dict` 파생형

  ```python
  from collections import Counter
  freq = Counter(a_list)
  ```
* **중첩 dict** 다룰 땐 `dict.setdefault` 활용

  ```python
  d = {}
  d.setdefault('group', {}).setdefault('sub', []).append(item)
  ```
* **정렬된 dict** 가 필요하면 `collections.OrderedDict`, Python 3.7+ 에선 기본 dict도 삽입 순 보장

---

### ✔️ 정리 팁

1. **예제 코드** 를 직접 타이핑해 보고, **메서드별 반환값** 을 확인하세요.
2. **시간 복잡도** 를 외우기보다는 “append 빠르고 insert 느리다” 정도로 체감하세요.
3. **자주 쓰는 패턴** (컴프리헨션, enumerate, zip, Counter) 위주로 손에 익히면 코딩 테스트에서도 속도가 빨라집니다.

---