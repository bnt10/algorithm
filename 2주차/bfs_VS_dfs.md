

## 1. 문제에서 요구하는 결과의 성격

| 요구되는 결과           | 주로 쓰는 탐색 방식    | 이유                                            |
| ----------------- | -------------- | --------------------------------------------- |
| 최단 경로(최소 간선 수) 찾기 | **BFS**        | 레벨별로 넓게 탐색하므로, 처음 만나는 목표가 무조건 최단 경로임          |
| 레벨(깊이)별 처리·계산     | **BFS**        | “시작점에서 거리가 1인 노드 → 거리 2인 노드…” 순으로 순차적 처리 가능   |
| 연결 요소의 크기 세기      | BFS·DFS 모두 가능  | 크기만 세면 되므로 어느 쪽이든 상관없음                        |
| 경로 존재 여부(도달 가능성)  | BFS·DFS 모두 가능  | 둘 중 편한 방법으로 쓰되, 되도록 스택(재귀) 쓰면 구현이 간결한 DFS 추천  |
| 모든 경로·조합을 완전 탐색   | **DFS** (백트래킹) | “가지 뻗어 들어간 뒤 전부 탐색(backtrack)” 구조가 자연스러움      |
| 위상 정렬·사이클 검출·매칭 등 | **DFS**        | 재귀 호출을 이용한 트리 구조·후위 처리(post-order)가 필수인 경우 많음 |

---

## 2. 메모리·시간 제약

* **BFS**

    * Frontier(큐)에 한 레벨의 모든 노드를 담으므로 **메모리 사용량**이 클 수 있음
    * 그러나 레벨 단위로 한 번에 확장하므로 **깊이가 크지 않을 때** 유리
* **DFS**

    * 스택(또는 재귀)으로 “깊이 우선”으로 들어가기 때문에 메모리는 **경로 길이**(최대 깊이) 수준만 필요
    * 하지만 **무한 루프**나 **너무 깊은 재귀**에 주의해야 함

---

## 3. 탐색 구조의 복잡성

* **조건부로 “가장 먼저 찾은 답”을 바로 반환**해야 한다면

    * 그 답이 “최단” 혹은 “레벨별 첫 등장”이어야 할 경우 → **BFS**
    * “어떤 답이라도 찾으면 된다”(경로 존재 확인 등) → **DFS**로 간단히 구현 가능
* **모든 해(답)를 다 모아서 처리**해야 한다면

    * “모든 경로 합산”, “모든 조합 나열” 같이 **완전 탐색**이 필요할 때 → **DFS(백트래킹)**
* **연결 요소의 크기·합계 등을 계산**해야 할 때

    * 순서를 고려하지 않는 단순 방문 카운팅 → **BFS/DFS 양쪽 다 OK**

---

### 결론적으로…

1. **“최단” 혹은 “레벨별” 성격** → **BFS**
2. **“모두” 혹은 “깊이 우선 조합” 성격** → **DFS**
3. **단순 연결 요소 크기 계산** → 편한 쪽으로(대부분 BFS)
4. **메모리 제약이 엄격하고 깊이가 얕거나 경로 존재만 확인** → **DFS**

이 기준을 떠올리면, 문제를 읽을 때

> “내가 찾으려는 건 최단인가?
> 아니면 가능한 모든 해를 나열해야 하나?”

라는 질문을 먼저 던지고, 그에 맞춰 **BFS vs DFS**를 골라 적용하시면 됩니다.
