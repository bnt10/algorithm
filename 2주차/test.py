from itertools import combinations
def solution(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n**0.5) + 1 , 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    return sum([1 for a,b,c in combinations(nums,3) if is_prime(a+b+c)])

print(solution([1,2,3,4]))
    