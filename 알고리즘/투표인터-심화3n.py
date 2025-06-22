from math import inf
from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()                                # R: 정렬
    n = len(nums)
    best_diff, best_sum = inf, 0               # S 초기화

    for i in range(n - 2):                     # D: i 고정
        l, r = i + 1, n - 1                    # S: 포인터
        while l < r:
            curr = nums[i] + nums[l] + nums[r]     # O-1
            diff = abs(curr - target)
            if diff < best_diff:               # O-2: 갱신
                best_diff, best_sum = diff, curr
                if diff == 0:                  # T: 완전 일치
                    return best_sum

            if curr < target:                  # O-3: 포인터 이동
                l += 1
            else:
                r -= 1

    return best_sum                            # G


from math import inf
from typing import List

def threeSumCloset(nums: List[int], target:int) -> int:
    nums.sort()
    n = len(nums) # 4
    best_diff, best_sum = inf, 0

    for i in range(n - 2):
        l, r = i + 1 , n - 1

        while l < r:
            curr = nums[i] + nums[l] + nums[r]
            diff = abs(curr - target)
            if diff < best_diff:
                best_diff , best_sum = diff, curr
                if diff == 0:
                    return best_sum
                if curr < target:
                    l += 1
                else:
                    r -= 1
    return best_sum

def solution(nums, target):
    nums.sort()
    n = len(nums)
    best_diff, best_sum = inf , 0
    for i in range(n - 2) :
        l,r = i +1 , n-1
        while l < r:
            curr = nums[i] + nums[l] + nums[r]
            diff = abs(curr - target)
            if  diff < best_diff:
                best_diff , best_sum = diff, curr
                if diff == 0:
                    return best_sum
                if curr < target:
                    l += 1
                else:
                    r -= 1
