import sys

N = int(sys.stdin.readline())
a  = sorted(map(int, sys.stdin.readline().split()))

l, r = 0, N - 1
best_sum = abs(a[l] + a[r])
best_pair = (a[l], a[r])

while l < r:
    curr = a[l] + a[r]

    # (2) 최적값 갱신
    if abs(curr) < best_sum:
        best_sum = abs(curr)
        best_pair = (a[l], a[r])
        if best_sum == 0:          # 완전 0이면 최선 → 즉시 종료
            break

    # (3) 포인터 이동
    if curr < 0:
        l += 1                     # 합이 음수 → 더 큰 값 필요
    else:
        r -= 1                     # 합이 양수 → 더 작은 값 필요

print(*best_pair)


import sys
N = int(sys.stdin.readline())
a  = sorted(map(int, sys.stdin.readline().split()))

l, r = 0, N -1

best_sum = abs(a[l]+a[r])
best_pair = (a[l],a[r])

while l < r:
    curr = a[l] + a[r]

    if abs(curr) < best_sum:
        best_sum = abs(curr)
        best_pair = (a[l],a[r])
        if best_sum == 0:
            break

    if curr < 0:
        l += 1
    else:
        r -= 1
print(*best_pair)

