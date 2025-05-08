20초 동안 생각함


## 🧠 코딩 테스트 문제 학습 템플릿 — **“위장”** (프로그래머스 Lv. 2)

---

## 📌 문제 정보

* 🔹 문제명: **위장**
* 🔹 사이트: **프로그래머스 Lv. 2**
* 🔹 문제 링크: [https://school.programmers.co.kr/learn/courses/30/lessons/42578](https://school.programmers.co.kr/learn/courses/30/lessons/42578)

---

## 🔍 문제 설명 (공식 그대로)

> 스파이가 하루에 입을 수 있는 옷의 조합 수를 계산한다.
>
> * 옷은 (이름, 종류) 튜플로 주어진다.
> * 각 종류별로 최대 한 벌만 착용할 수 있다.
> * **아무것도 안 입는 경우는 제외**한다.
>
> **조합 수**를 반환하라.

### 📥 입력

```python
clothes: List[List[str]]  # 길이 1 ~ 30
# clothes[i] = [의상_이름, 의상_종류]
```

### 📤 출력

```python
answer: int  # 가능한 서로 다른 옷차림의 개수
```

### 📌 조건 요약

* 같은 종류 옷은 동시에 착용 불가 (0 또는 1 벌).
* 종류가 `k` 개라면, **종류 별 (선택 개수 + 1)** 의 곱 − 1(모두 미착용)

### 📐 수식화

$$
\text{answer} \;=\;\Bigl(\prod_{t\in\text{종류}}(cnt_t + 1)\Bigr)\;-\;1
$$

---

## 🧠 아이디어 도출 — 3 행으로 끝낸다

| 단계           | 내용                                     |
| ------------ | -------------------------------------- |
| **① 카운팅**    | 종류별 옷 개수 → `dict`(`get` 또는 `Counter`). |
| **② 곱셈**     | 각 종류 `cnt+1`(안 입는 옵션) 곱.               |
| **③ 공집합 제외** | 최종 곱 − 1.                              |

#### 예시 시뮬레이션

```
clothes = [
  ["yellow_hat",  "headgear"],
  ["blue_sung",   "eyewear"],
  ["green_turban","headgear"]
]
종류별 = {"headgear":2, "eyewear":1}
(2+1)*(1+1) - 1 = 3*2 - 1 = 5
```

---

## 🧱 구현 계획

* **자료구조**: `dict` + `get`, 또는 `defaultdict(int)`
* **주요 변수**

  * `counter` : `{종류: 개수}`
  * `answer` : 누적 곱
* **복잡도**

  * 시간 `O(N)` (N ≤ 30) | 공간 `O(K)` (종류 ≤ 30)

---

## ✅ 코드 (Python 3, 설명 주석 포함)

```python
from collections import Counter
from functools import reduce
import operator

def solution(clothes):
    # 1) 종류별 개수 집계
    kind_cnt = Counter(kind for _, kind in clothes)
    
    # 2) (cnt + 1) 곱산 (functools.reduce 사용)
    total = reduce(operator.mul,
                   (cnt + 1 for cnt in kind_cnt.values()),
                   1)
    # 3) 전부 미착용 케이스 제외
    return total - 1
```

> **한 줄 버전** *(가독성 ↓ 실전 권장 X)*
>
> ```python
> def solution(clothes):
>     from collections import Counter
>     from functools import reduce
>     import operator
>     return reduce(operator.mul, (c+1 for c in Counter(k for _,k in clothes).values()), 1) - 1
> ```

---

## 🧪 테스트 및 디버깅

| 케이스      | 입력                          | 예상 출력      | 이유           |
| -------- | --------------------------- | ---------- | ------------ |
| ① 예제     | `[["a","a"],["b","b"]]`     | 3          | (1+1)(1+1)−1 |
| ② 한 종류   | `[["a","hat"],["b","hat"]]` | 2          | (2+1)−1      |
| ③ 종류=3 개 | 10 벌 분산                     | ∏(cnt+1)−1 | 다중 곱 검증      |
| ④ 최소 입력  | `[["x","mask"]]`            | 1          | 단일 종류 1 벌    |

> **디버그 팁**
> `print(kind_cnt)` → `{종류:개수}` 확인 후 곱을 수작업 검산.

---

## 📖 정답 코드 리뷰

* **자료구조 선택**: 해시 → 상수 조회.
* **곱셈 연산**: `reduce + operator.mul` 이 가장 간결. `for` 루프 누적도 동일 성능.
* **공집합 제외**: 시험에서 잊기 쉬운 함정 #1.

---

## 💡 학습 포인트 정리

1. **종류별 카운트 → 곱셈 → −1** : “선택+1 ×, 공집합‑1” 공식화 습관.
2. `Counter` · `defaultdict` 로 **카운트 코드 2 줄**로 압축.
3. **곱 누적** 패턴 (`reduce`, `math.prod`\[Py 3.8+]) 은 Lv 3 이상 문제에 반복 출현.

---

## 🔁 복습 스케줄

* [ ] 내일 : 빈 에디터 → 8 분 내 재구현
* [ ] 3일 뒤 : 변형 조건(공집합 포함 가능? 복수 선택?) 문제 자작 후 풀이
* [ ] 1주일 뒤 : `dict` 카운팅 문제(Anagrams, 베스트셀러) 묶어 복습

**→ 지금 타이머 15 분**: 빈 파일에서 위 코드를 재타이핑, 추가 테스트 4 개 통과 후 마무리.
