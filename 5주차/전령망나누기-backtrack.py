from collections import defaultdict

def solution(n, wires):
    def dfs(node, visited, graph):
        visited[node] = True
        count = 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                count += dfs(neighbor, visited, graph)
        return count

    min_diff = n  # 최대 차이 초기값
    for i in range(len(wires)):
        # 1) 간선 i 제거한 그래프 생성
        graph = defaultdict(list)
        for j in range(len(wires)):
            if i == j:
                continue
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)

        # 2) 연결된 컴포넌트 크기 계산
        visited = [False] * (n + 1)
        count = dfs(1, visited, graph)

        # 3) 차이 계산
        diff = abs(n - 2 * count)
        min_diff = min(min_diff, diff)

    return min_diff




def solution1(n , wires):
    def dfs(node,visited,graph):
        visited[node] = True
        count = 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                count += dfs(neighbor, visited,graph)
        return count

    min_diff = n
    for i in range(len(wires)):
        graph = defaultdict(list)
        for j in range(len(wires)):
            if i == j:
                continue
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * (n + 1)
        count = dfs(1, visited,graph)

        diff = abs(n - 2 * count)
        min_diff = min(min_diff, diff)
    return  min_diff

#아이디언는 현재 인풋 자체는 그래프로 변경 가능하다
#이때 입력정보는 간선이기 때문에 하나의 간선을 제거하고 전체를 구하

def solution(n, wires):

    def dfs(node,visited,graph):
        visited[node] = True
        count = 1
        for adj in graph[node]:
            if not visited[adj]:
                count += dfs(node,visited,graph)
        return  count

    min_diff = n
    for i in range(len(wires)):
        graph = defaultdict(list)
        for j in range(len(wires)):
            if i == j:
                continue
            u,v = wires[j]
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (n + 1)
        count = dfs(1,visited,graph)

        diff = abs(n - 2 * count)
        min_diff = min(min_diff,diff)


"""
전력망을 나누고 싶다

주어진 input은 간선을 표현하고 있다.
각 간선을 한번씩 뺀 그래프를 만들어서 각각의 그래프의 크기를 구하면?

각 간선을 빼보기

"""

def soultion(n,wires):
    min_dff = n
    for i in range(len(wires)):
        graph = defaultdict(list)

        for j in range(len(wires)):
            if  i == j:
                continue
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)








