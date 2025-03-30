"""
개념

이분 탐색(Binary Search)은 정렬된 배열에서 특정 값을 효율적으로 찾는 알고리즘 입니다.
배열을 절반으로 나누면서 찾고자 하는 값이 왼쪽 절반에 있는지, 오른쪽 절반에 있는지를
반복적으로 확인하는 방식입니다. 시간 복잡도는 O(log N) 으로 매우 빠릅니다.


동작 방식

1. 배열이 정렬되어 있어야 한다.
2. 탐색 범위를 설정한다 (초기 low =0, high = len(arr) - 1)
3. 중간값을 찾는다. (mid = (low + high) // 2)
4. 비교 후 탐색 범위를 좁힌다.

 - arr[mid] == target 이면 값이 존재하므로 반환
 - arr[mid] < target 이면 low = mid + 1 (오른쪽에서 탐색)
 - arr[mid] > target 이면 high = mid - 1 (왼쪽에서 탐색)

5. 반복하여 찾을 때까지 또는 low > high가 될 때까지 진행한다.
"""

#예시
arr = [1,3,5,7,9,11,13,15]
target = 7

def binary_search(arr,target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return  mid # target을 찾은 경우
        elif arr[mid] < target:
            low = mid + 1 # 오른쪽에서 탐색
        else:
            high = mid - 1 # 왼쪽에서 탐색
    return  -1 # target이 없는 경우

result = binary_search(arr,target)
print(result) # 3 (7이 저장된 인덱스)
