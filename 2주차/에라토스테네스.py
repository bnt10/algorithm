from itertools import permutations

def solution(numbers: str) -> int:
    # 1) 순열 생성 & 중복 제거
    perms = set()
    for k in range(1, len(numbers) + 1):
        for p in permutations(numbers, k):
            perms.add(int(''.join(p)))
    if not perms:
        return 0

    # 2) 에라토스테네스의 체
    max_n = max(perms)

    sieve = [True] * (max_n + 1)

    sieve[0:2] = [False, False]
    m = int(max_n**0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            print([False] * (((max_n - i*i)//i) + 1))
            sieve[i*i : max_n+1 : i] = [False] * (((max_n - i*i)//i) + 1)

    # 3) 소수 개수 반환

    return sum(1 for num in perms if sieve[num])

print(solution("011"))



