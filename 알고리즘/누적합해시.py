import sys
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

cnt_map = defaultdict(int)
cnt_map[0] = 1          # Ps[0] = 0 존재
prefix = 0
answer = 0

for x in A:                                 # D: 한 칸 전진
    prefix += x                             # O-1
    answer += cnt_map[prefix - K]           # O-2
    cnt_map[prefix] += 1                    # O-3

print(answer)
