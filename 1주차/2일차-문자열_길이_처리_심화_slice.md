# 문자열 압축

---

## 📌 문제 정보

* 🔹 문제명: 문자열 압축
* 🔹 사이트: [프로그래머스]
* 🔹 문제 링크: [https://school.programmers.co.kr/learn/courses/30/lessons/60057](https://school.programmers.co.kr/learn/courses/30/lessons/60057)

---

## 🔍 문제 요약

* 📥 입력: 문자열 `s`
* 📤 출력: 1개 이상 단위로 문자열을 잘라 압축한 문자열 중 가장 짧은 길이 (정수)
* 📌 조건 요약:

    * 1 ≤ s의 길이 ≤ 1,000
    * s는 알파벳 소문자로만 구성
* 📐 수식화 시도:

    * 단위를 `1 ≤ 단위 ≤ len(s) // 2`로 나눠가며 문자열을 쪼갠다.
    * 각 단위마다 앞에서부터 같은 단위 문자열이 연속되는 횟수를 세어 압축.
    * 압축된 문자열의 길이를 모두 비교하여 최소값을 리턴.

---

## 🧠 아이디어 도출

* 예시 테스트 케이스 직접 시뮬레이션:

```
예제 입력: "aabbaccc"
→ 단위 1: a a b b a c c c → "2a2ba3c" → 길이: 7
→ 단위 2: aa bb ac cc → "aabbaccc" → 길이: 8
→ 단위 3: aab bac cc → "aabbaccc" → 길이: 8
결과: 7

예제 입력: "ababcdcdababcdcd"
→ 단위 1~8까지 시도해서 가장 짧은 길이: 9
```

* 떠오른 알고리즘 유형:
  ✅ Brute-force (완전탐색)
* 문제를 단계로 나눈다면?

    1. 단위 길이를 1부터 절반까지 증가시키며 반복
    2. 같은 문자열이 연속되는지 확인
    3. 압축된 문자열 구성
    4. 그 중 최소 길이 찾기

---

## 🧱 구현 계획

* 사용할 자료구조: 문자열 (문자열 누적)
* 사용할 주요 변수:

    * `unit`: 압축 단위
    * `compressed`: 압축 문자열
    * `prev`, `count`: 현재 비교 중인 문자열, 반복 수
* 핵심 반복 / 조건:

    * `for unit in range(1, len(s)//2 + 1)`
    * `for i in range(unit, len(s), unit)`

---

## ✅ 코드

```python
def solution(s):
    min_len = len(s)  # 압축을 하지 않았을 때의 길이로 초기화

    for unit in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[:unit]  # 첫 덩어리
        count = 1

        for i in range(unit, len(s), unit):
            curr = s[i:i+unit]
            if curr == prev:
                count += 1
            else:
                compressed += str(count) + prev if count > 1 else prev
                prev = curr
                count = 1

        # 마지막 덩어리 처리
        compressed += str(count) + prev if count > 1 else prev

        min_len = min(min_len, len(compressed))

    return min_len
```

---

## 🧪 테스트 및 디버깅

```
print(solution("aabbaccc"))                # 7
print(solution("ababcdcdababcdcd"))        # 9
print(solution("abcabcdede"))              # 8
print(solution("abcabcabcabcdededededede"))# 14
print(solution("xababcdcdababcdcd"))       # 17
```

* 예제 테스트 결과: ✅ 모두 정답
* 실패 케이스: 없음
* 발견한 문제 원인: 없음

---

## 📖 정답 코드 리뷰

* 내가 떠올리지 못한 아이디어: 없음 — brute-force로도 해결 가능
* 정답이 쓰는 핵심 알고리즘: **시뮬레이션 + 완전탐색**

---

## 💡 학습 포인트 정리

* 단위 길이를 변화시키며 문자열을 쪼개는 방식 자체가 핵심 포인트.
* 문자열을 다루는 문제에서 **부분 문자열 + 반복 횟수 계산**이 자주 쓰임.
* 이 문제는 Greedy 또는 DP가 아니라, **시뮬레이션 문제**임을 잘 구분하자.
* 문제 유형 분류: ✅ 문자열, 완전탐색, 시뮬레이션

---

## 🔁 복습 예정일

* [ ] 내일
* [ ] 3일 뒤
* [ ] 1주일 뒤

---

필요하시면 비슷한 유형의 문자열 시뮬레이션 문제도 추천해드릴게요.
다음으로 어떤 문제를 풀어보고 싶으신가요?
