7초 동안 생각함


## 🧠 코딩 테스트 문제 학습 템플릿 – “폰켓몬” (프로그래머스 Lv. 1)

---

## 📌 문제 정보

* 🔹 문제명: **폰켓몬**
* 🔹 사이트: **프로그래머스 Lv. 1**
* 🔹 문제 링크: [https://school.programmers.co.kr/learn/courses/30/lessons/1845](https://school.programmers.co.kr/learn/courses/30/lessons/1845)

---

## 🔍 문제 설명 (공식 그대로)

> 당신은 N 마리의 폰켓몬(종 번호로 표현되는 정수) 중에서 **N / 2** 마리를 가져갈 수 있다.
> 가능한 한 **서로 다른 종류**(서로 다른 숫자)의 폰켓몬을 많이 선택할 때, 선택할 수 있는 **가장 큰 종류 수**를 반환하라.

### 📥 입력

* 정수 배열 `nums` (1 ≤ `len(nums)` ≤ 100 000)

    * `nums[i]` 는 폰켓몬의 “종” 번호 (음수·중복 허용)

### 📤 출력

* 정수 하나 `answer` : 선택 가능한 최대 **서로 다른 폰켓몬 종류 개수**

### 📌 조건 요약

* 가져가는 수 = `len(nums) // 2`
* 같은 종은 여러 마리 존재 가능
* 목표 → **종류 수** 최대화

### 📐 수식화

* `k = len(nums)//2`
* `unique = |set(nums)|`
* `answer = min(unique, k)`

---

## 🧠 아이디어 도출

| 단계            | 사고 과정                                            |
| ------------- | ------------------------------------------------ |
| **① 중복 제거**   | 종류만 카운트하면 되므로 `set(nums)` 사용.                    |
| **② 선택 수 제한** | 가져갈 수 있는 최대 마리 수 = `N/2`. 종류가 이보다 많아도 넘치면 못 가져감. |
| **③ 최종 공식**   | `min(종류수, N/2)` 가 최대 종류 수. – 끝.                  |

### 예시 시뮬레이션

```
nums = [3,3,3,2,2,4]  # N=6 → k=3
종류 = {2,3,4} → 3종
answer = min(3, 3) = 3
```

---

## 🧱 구현 계획

* **자료구조**: `set` (해시 O(1) 조회)
* **주요 변수**

    * `k` : 선택 가능 마리 수
    * `species_cnt` : 고유 종 개수
* **핵심 로직**

  ```python
  k = len(nums)//2
  species_cnt = len(set(nums))
  return min(species_cnt, k)
  ```

---

## ✅ 코드 (주석 필수, 깔끔 4줄이면 충분)

```python
def solution(nums):
    # 1) 선택 가능한 총 마리 수 (반 절)
    k = len(nums) // 2
    
    # 2) 서로 다른 종 수
    species_cnt = len(set(nums))
    
    # 3) 가져갈 수 있는 최대 종류 = 종류 수 vs 마리 수 중 더 작은 값
    return min(species_cnt, k)
```

---

## 🧪 테스트 & 디버깅

| 케이스   | 입력                      | 예상  | 이유                       |
| ----- | ----------------------- | --- | ------------------------ |
| 기본    | `[3,1,2,3]`             | 2   | 종류=3, k=2                |
| 모두 동일 | `[1,1,1,1]`             | 1   | 종류=1, k=2                |
| 모두 다름 | `[1,2,3,4]`             | 2   | 종류=4, k=2                |
| 대량 중복 | `[1]*50000 + [2]*50000` | 2   | 종류=2, k=100 000/2=50 000 |

---

## 📖 정답 코드 리뷰

* **핵심 알고리즘**: *집합 → 최솟값* ‑ 해시 이용 O(N)
* 더 빠를 방법? 없다. 이미 O(N) / O(N) 메모리 (집합)

---

## 💡 학습 포인트 정리

1. **“최대 고유 개수 vs 선택 제한” → `min()` 패턴**
2. **집합으로 중복 제거**: 리스트 길이 10⁵ 까지 여유.
3. **조건 파싱 능력**: “N/2 마리만”이라는 제약을 바로 수식에 끼워넣어라.

---

## 🔁 복습 예정일 체크

* [ ] 내일 (재타이핑 2 분 컷 목표)
* [ ] 3일 뒤 (조건 바꿔 변형 문제 만들기)
* [ ] 1주일 뒤 (비슷한 해시·중복 제거 문제와 묶어 리뷰)
