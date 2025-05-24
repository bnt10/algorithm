from collections import defaultdict, deque

def solution(n, wires):
    # 1) 그래프 구성 (양방향)
    graph = defaultdict(list)

    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)

    def bfs_count(start, block_u, block_v):
        """block_u-block_v 간선을 무시하고 start에서 연결된 노드 수를 BFS로 센다."""
        visited = set([start])
        queue = deque([start])

        count = 0

        while queue:
            node = queue.popleft()
            count += 1
            for adj in graph[node]:
                # 차단된 간선을 건너뛰기
                if (node == block_u and adj == block_v) or (node == block_v and adj == block_u):
                    continue
                if adj not in visited:
                    visited.add(adj)
                    queue.append(adj)
        return count

    answer = n  # 최대 차이로 초기화
    # 2) 각 간선을 빼 보며
    for u, v in wires:
        size1 = bfs_count(start=u, block_u=u, block_v=v)
        size2 = n - size1
        answer = min(answer, abs(size1 - size2))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
"""
[1,2] 를 제외하고 좌우를 나눠서 계산 해야 할텐데
[1,2] 면 1번 -> 2번 방향으로 탐색을 시작하는거지

그럼 1번과 연결되어 있는걸 찾되 1,2를 제외하고 찾으면 되겠네

1번 2번 이 포함안되고 
탐색 순서를 적어보자
[1,2],[2,4],[4,6]

2 ,4 를 탐색해야 하는데
여기서 2로 시작하려면

1 -> 2 > 4가 되어야 한다면


1 : 2
2 : 4

여기가 내가 모르는 시점인데 어떻게 시작할껀지



시작은 1 이고 
1,2 는 해당 연결된 점

1,2,4 를 그래프로 표현하면

1:[2]
2:[4]

1 다음에 2로 가는 방법 코드로 바꾸면?
[1,2],[2,3] 이런 배열이 있을때

for u,v in wires:
   stack = ]
   visited = set([1])
   while stack:
    node = pop
    if u == 1 and v ==2:
        continue
    if u not visited:
        visited.add(u)
    if v not visited:
        visited.add(v)
    

1 => 2 => 4는
1과 연결된 2
2와 연결되 4
4와 ..
이건 
"""
