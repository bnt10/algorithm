**문제 풀이 방향 잡기**

문제는 "완주하지 못한 선수"로, 참가자 목록과 완료자 목록을 주고 못 끝낸 선수 한 명을 찾는 문제입니다. 풀이 아이디어는 리스트나 해시맵을 이용해 참가자 수를 세고, 완료자 목록에서 뺀 결과를 그냥 반환하면 쉽게 해결할 수 있습니다.

세부 구현 방법과 템플릿을 따를 때는 반복문을 사용해 하나씩 비교하거나, 해시맵으로 완료 여부를 체크하는 방법을 쓸 수 있어요. 이 과정에서 세부 코딩 주석을 추가해야 합니다.

**문제 풀이 템플릿**

---

## 📌 문제 정보

* 🔹 문제명: 완주하지 못한 선수
* 🔹 사이트: 프로그래머스
* 🔹 문제 링크: [프로그래머스 42576](https://school.programmers.co.kr/learn/courses/30/lessons/42576)

---

## 🔍 문제 요약

* 📥 입력: 두 개의 리스트, 참가자 목록과 완료자 목록
* 📤 출력: 한 명의 이름 (완료하지 못한 선수)
* 📌 조건 요약: 참가자 목록에는 복잡한 중복이 있을 수 있음, 두 목록 비교 필요
* 📐 수식화 시도: 리스트 간 차이 또는 해시맵 비교

---

## 🧠 아이디어 도출

* 예시 테스트 케이스:

```
예제 입력: ["leo", "kiki", "eden"], ["eden", "kiki"]
예상 출력: "leo"
직접 풀이 과정: 반복문 등을 통해 완료자 목록에서 빼고, 나머지 남은 사람 출력
```

* 떠오른 알고리즘 유형: 해시맵
* 문제를 단계로 나눠본다면? 1) 목록 비교 2) 최종 결과 추출

---

## 🧱 구현 계획

* 사용할 자료구조: 해시맵
* 사용할 주요 변수: participants, completions
* 핵심 반복 / 조건: 한 명씩 비교 후 찾기

---

## ✅ 코드

```python
def solution(participants, completions):
    participants_dict = {}
    for participant in participants:
        participants_dict[participant] = participants_dict.get(participant, 0) + 1
    for completion in completions:
        participants_dict[completion] -= 1
    for participant, count in participants_dict.items():
        if count > 0:
            return participant
```

---

## 🧪 테스트 및 디버깅

* 예제 테스트 결과: 성공
* 실패 케이스: 없음
* 발견한 문제 원인: 없음

---

## 📖 정답 코드 리뷰

* 내가 떠올리지 못한 아이디어: 없음
* 정답이 쓰는 핵심 알고리즘: 해시맵을 이용해 참가자 목록을 카운팅하고, 완료자의 카운트를 빼는 방식

---

## 💡 학습 포인트 정리

* 왜 못 풀었는가? 문제를 어떻게 처리할지 몰랐을 때
* 다음에 이 유형을 보면 어떤 접근을 떠올려야 하나? 해시맵 활용
* 문제 유형 분류: 자료구조 (해시맵)

---

## 🔁 복습 예정일

* [ ] 내일
* [ ] 3일 뒤
* [ ] 1주일 뒤


27초 동안 생각함


## 🧠 코딩 테스트 문제 학습 템플릿

---

## 📌 문제 정보

* 🔹 **문제명**: 완주하지 못한 선수
* 🔹 **사이트**: 프로그래머스 Lv. 1
* 🔹 **문제 링크**: [https://school.programmers.co.kr/learn/courses/30/lessons/42576](https://school.programmers.co.kr/learn/courses/30/lessons/42576)

---

## 🔍 문제 요약

* 📥 **입력**:

    * `participant`: 대회에 참여한 선수 이름들이 담긴 문자열 배열 (길이 N, 중복 가능)
    * `completion`: 완주한 선수 이름들이 담긴 문자열 배열 (길이 N–1)
* 📤 **출력**:

    * 완주하지 못한 선수의 이름(문자열)
* 📌 **조건 요약**:

    1. 동일한 이름을 가진 선수가 여럿 있을 수 있다.
    2. `participant` 에는 반드시 한 명이 `completion` 에서 빠진 상태이다.
    3. 문자열은 알파벳 소문자로만 구성.
* 📐 **수식화 시도**:

    * 모든 이름 s 에 대해

      $$
      \text{count}_p(s) - \text{count}_c(s) =
      \begin{cases}
      1, & \text{s가 완주하지 못한 선수}\\
      0, & \text{그 외}
      \end{cases}
      $$

---

## 🧠 아이디어 도출

* **예시 테스트 케이스 직접 시뮬레이션**:

  ```
  예제 입력:
  participant = ["leo", "kiki", "eden"]
  completion  = ["eden", "kiki"]
  예상 출력:
  "leo"

  직접 풀이 과정:
  1. 참가자 이름별 등장 횟수: {leo:1, kiki:1, eden:1}
  2. 완주자 이름별 등장 횟수 차감:
     - eden → {leo:1, kiki:1, eden:0}
     - kiki → {leo:1, kiki:0, eden:0}
  3. 등장 횟수가 1인 이름 = "leo"
  ```

* **떠오른 알고리즘 유형**: 해시맵(Hash Map)을 이용한 카운팅

* **문제를 단계로 나눠본다면?**

    1. `participant` 순회하며 이름별 카운트 상승
    2. `completion` 순회하며 이름별 카운트 하강
    3. 최종적으로 카운트가 1인 이름 반환

---

## 🧱 구현 계획

* **사용할 자료구조**:

    * `dict` (이름 → 등장 횟수) 또는 `collections.Counter`
* **사용할 주요 변수**:

    * `count_map`: 각 이름의 남은 등장 횟수를 저장
* **핵심 반복 / 조건**:

    1. `for name in participant:` → `count_map[name] += 1`
    2. `for name in completion:`  → `count_map[name] -= 1`
    3. `for name, cnt in count_map.items(): if cnt > 0: return name`

---

## ✅ 코드

```python
from collections import defaultdict

def solution(participant, completion):
    # 1) 참가자 이름별 등장 횟수 카운팅
    count_map = defaultdict(int)
    for name in participant:
        count_map[name] += 1

    # 2) 완주자 이름별 등장 횟수 차감
    for name in completion:
        count_map[name] -= 1

    # 3) 등장 횟수가 1인(=완주하지 못한) 선수 이름 반환
    for name, cnt in count_map.items():
        if cnt > 0:
            return name
```

---

## 🧪 테스트 및 디버깅

* **예제 테스트 결과**:

    * `["leo","kiki","eden"], ["eden","kiki"]` → `"leo"` (통과)
* **추가 실패 케이스**:

    * 중복 이름

      ```python
      participant = ["mislav","stanko","mislav","ana"]
      completion  = ["stanko","ana","mislav"]
      # 예상 출력: "mislav"
      ```
* **발견한 문제 원인**:

    * 중복 이름 처리 미흡 시, 단순 집합 사용은 오류 발생

---

## 📖 정답 코드 리뷰 (필요 시)

* **내가 떠올리지 못한 아이디어**:

    * 두 리스트를 정렬한 뒤 인덱스별 비교(차집합)로 한 번에 찾기

      ```python
      participant.sort()
      completion.sort()
      for p, c in zip(participant, completion):
          if p != c:
              return p
      return participant[-1]
      ```
* **정답이 쓰는 핵심 알고리즘**:

    * 해시맵 기반 카운팅 또는 정렬 기반 비교

---

## 💡 학습 포인트 정리

* **왜 못 풀었는가?**

    * 동일 이름이 여러 번 등장하는 경우를 고려하지 않음
* **다음에 이 유형을 보면 어떤 접근을 떠올려야 하나?**

    * “등장 횟수 차이” 가 핵심이므로, 카운팅 기법을 먼저 떠올린다
* **문제 유형 분류**:

    * **해시(Hash)**, **카운팅(Counting)**

---

## 🔁 복습 예정일

* [ ] 내일
* [ ] 3일 뒤
* [ ] 1주일 뒤

---
