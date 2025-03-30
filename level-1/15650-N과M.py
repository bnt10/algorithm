# 조합을 dfs , backtracking 으로 구현

import sys

# input = sys.stdin.readline
#
# n, m = map(int , input().split())
#
# arr = [i for i in range(1, n + 1)]
# r = 2
# result = []
# visited = [False] * len(arr)
#
# def combinations(current):
#     if len(current) == r:
#         result.append(current[:])
#         return
#     for i in range(len(arr)):
#         if not visited[i]:
#             visited[i] = True
#             current.append(arr[i])
#             combinations(current)
#             current.pop()
#             visited[i] = False
#
# combinations([])
# print(result)

# 순연

import sys
input = sys.stdin.readline
n , m = map(int, input().split())

arr = [i for i in range(1, n+1)]
r = 2
result = []

def permutation(start, current):
    if len(current) == r:
        result.append(current[:])
        return

    for i in range(start, len(arr)):
        current.append(arr[i])
        permutation(i + 1 , current)
        current.pop()


permutation(0,[])
print(result)