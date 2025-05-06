
# 시저 암호

---

## 📌 문제 정보

- 🔹 문제명: 시저 암호
- 🔹 사이트: [프로그래머스]
- 🔹 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12926

---

## 🔍 문제 요약

- 📥 입력: 변경할 문자열 s , shift 단위 n
- 📤 출력: shift 한 문자열
- 📌 조건 요약:
  - 공백은 유지
  - 대문자, 소문자 구분 필요
  - z + n 된 경우 다시 a 으로 시작
- 📐 수식화 시도: 
  - 대소문자 구분 필요
  - 공백 유지 필요
  - z 이후 shift에 대한 처리가 필

---

## 🧠 아이디어 도출

- 예시 테스트 케이스 직접 시뮬레이션:

```
예제 입력: AB , 1
예상 출력: BC
직접 풀이 과정: 문자열을 shift 해서 처리
```

- 떠오른 알고리즘 유형: 문자열 처리 ord , chr 를 이용
- 문제를 단계로 나눠본다면?
1. 변경한 문자를 담을 result 변수
2. 입력 단어가 공백인지, 대문자, 소문자 인지 구별
3. shift 상태를 표현


---

## 🧱 구현 계획

- 사용할 자료구조: 문자열 처리
- 사용할 주요 변수:
  - result : 변경된 char를 담을 변수
- 핵심 반복 / 조건:
  - 대소문자 구별
  - shfit 처리
---

## ✅ 코드

```python

def solution(s, n):
  result = []
  for idx, char in enumerate(s):
    if char == ' ':
      result.append(char)
    if ord(char) - ord('A') < 26:
      result.append(chr(((ord(char)  - ord('A') + n ) % 26) + ord('A')))
    else :
      result.append(chr(((ord(char)  - ord('a') + n ) % 26) + ord('a')))


  return "".join(result)

print(solution("a B z",4))
```

---

## 🧪 테스트 및 디버깅

- 예제 테스트 결과: 정상 출력
- 실패 케이스: 없음
- 발견한 문제 원인: 없음

---

## 📖 정답 코드 리뷰 (필요 시)

- 내가 떠올리지 못한 아이디어:
```python
def caesar(s, n):
  s = list(s)
  for i in range(len(s)):
    if s[i].isupper():
      s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
    elif s[i].islower():
      s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

  return "".join(s)
  # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))
```
- 정답이 쓰는 핵심 알고리즘: 없음

---

## 💡 학습 포인트 정리

- 왜 못 풀었는가?
- 다음에 이 유형을 보면 어떤 접근을 떠올려야 하나?
- 문제 유형 분류: (ex. DFS, 백트래킹, 그리디 등)

---

## 🔁 복습 예정일

- [ ] 내일
- [ ] 3일 뒤
- [ ] 1주일 뒤
