from collections import deque

def diff_one(a, b) :
    """두 단어가 한 글자만 다르면 True"""
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solution(begin, target, words) :
    if target not in words:          # 사전에 없으면 불가능
        return 0

    q = deque([(begin, 0)])          # (현재 단어, 변환 횟수)
    visited = {begin}

    while q:
        cur, depth = q.popleft()
        if cur == target:            # 최초 도착 == 최단 경로
            return depth

        for w in words:
            if w not in visited and diff_one(cur, w):
                visited.add(w)
                q.append((w, depth + 1))

    return 0                         # 끝까지 못 찾음


deque